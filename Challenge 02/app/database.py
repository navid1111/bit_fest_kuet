from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = "mofas_kitchen_buddy"

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]

# Ensure indexes for better performance (optional but recommended)
# e.g., Create an index on ingredient name for faster searches
async def create_indexes():
    await db.ingredients.create_index([("name", ASCENDING)], unique=True)
    await db.recipes.create_index([("title", ASCENDING)], unique=True)
    
