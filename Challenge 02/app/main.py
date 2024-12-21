from fastapi import APIRouter, HTTPException, FastAPI
from typing import List

from .models import IngredientCreate, Ingredient
from .crud import create_ingredient, get_ingredient, update_ingredient, delete_ingredient, list_ingredients


router = APIRouter(
    prefix="/ingredients",
    tags=["Ingredients"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=Ingredient)
async def add_ingredient(ingredient: IngredientCreate):
    print(ingredient)
    existing = await get_ingredient(ingredient.name)
    if existing:
        raise HTTPException(status_code=400, detail="Ingredient already exists.")
    return await create_ingredient(ingredient)

@router.get("/", response_model=List[Ingredient])
async def get_all_ingredients():
    return await list_ingredients()

@router.put("/{name}", response_model=Ingredient)
async def update_existing_ingredient(name: str, quantity: float, unit: str):
    ingredient = await update_ingredient(name, quantity, unit)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found.")
    return ingredient

@router.delete("/{name}", response_model=dict)
async def delete_existing_ingredient(name: str):
    success = await delete_ingredient(name)
    if not success:
        raise HTTPException(status_code=404, detail="Ingredient not found.")
    return {"detail": "Ingredient deleted successfully."}


app = FastAPI()
app.include_router(router)