# app/models.py

from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from datetime import datetime

# Helper to handle ObjectId with Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# Ingredient Model
class IngredientBase(BaseModel):
    name: str = Field(..., example="Sugar")
    quantity: float = Field(..., example=2.5)
    unit: str = Field(..., example="kg")

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    last_updated: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Recipe Model
class RecipeIngredient(BaseModel):
    name: str = Field(..., example="Flour")
    quantity: float = Field(..., example=2)
    unit: str = Field(..., example="cups")

class RecipeBase(BaseModel):
    title: str = Field(..., example="Chocolate Cake")
    ingredients: List[RecipeIngredient]
    instructions: str = Field(..., example="Mix all ingredients and bake at 350°F for 30 minutes.")
    taste: str = Field(..., example="Sweet")
    cuisine_type: str = Field(..., example="Dessert")
    preparation_time: int = Field(..., example=45)  # in minutes
    reviews: Optional[int] = Field(0, example=10)

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
