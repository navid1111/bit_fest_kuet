# app/crud.py

from .database import db
from .models import IngredientCreate, Ingredient, RecipeCreate, Recipe
from typing import List, Optional

import datetime

# Ingredients
async def create_ingredient(ingredient: IngredientCreate) -> Ingredient:
    ingredient_dict = ingredient.model_dump()
    result = await db.ingredients.insert_one(ingredient_dict)
    ingredient_dict["_id"] = result.inserted_id
    ingredient_dict["last_updated"] = ingredient_dict.get("last_updated", ingredient_dict.get("last_updated"))
    return Ingredient(**ingredient_dict)

async def get_ingredient(name: str) -> Optional[Ingredient]:
    ingredient = await db.ingredients.find_one({"name": name})
    if ingredient:
        return Ingredient(**ingredient)
    return None

async def update_ingredient(name: str, quantity: float, unit: str) -> Optional[Ingredient]:
    update = {"$set": {"quantity": quantity, "unit": unit, "last_updated": datetime.utcnow()}}
    result = await db.ingredients.find_one_and_update({"name": name}, update, return_document=True)
    if result:
        return Ingredient(**result)
    return None

async def delete_ingredient(name: str) -> bool:
    result = await db.ingredients.delete_one({"name": name})
    return result.deleted_count > 0

async def list_ingredients() -> List[Ingredient]:
    ingredients = []
    async for ingredient in db.ingredients.find():
        ingredients.append(Ingredient(**ingredient))
    return ingredients

# Recipes CRUD

async def create_recipe(recipe: RecipeCreate) -> Recipe:
    recipe_dict = recipe.model_dump()
    result = await db.recipes.insert_one(recipe_dict)
    recipe_dict["_id"] = result.inserted_id
    recipe_dict["created_at"] = recipe_dict.get("created_at", datetime.utcnow())
    return Recipe(**recipe_dict)

async def get_recipe(title: str) -> Optional[Recipe]:
    recipe = await db.recipes.find_one({"title": title})
    if recipe:
        return Recipe(**recipe)
    return None

async def list_recipes() -> List[Recipe]:
    recipes = []
    async for recipe in db.recipes.find():
        recipes.append(Recipe(**recipe))
    return recipes
