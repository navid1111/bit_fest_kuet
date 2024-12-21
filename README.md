
Challenge 2:

Ingredients API
1. Get All Ingredients
Route: /ingredients/
Method: GET
Description: Retrieves a list of all available ingredients in the database.

[
  {
    "_id": "60d5f483f8d4e2a5b4e5c3d1",
    "name": "Sugar",
    "quantity": 2.5,
    "unit": "kg",
    "last_updated": "2024-12-21T10:00:00Z"
  },
  {
    "_id": "60d5f483f8d4e2a5b4e5c3d2",
    "name": "Flour",
    "quantity": 5.0,
    "unit": "kg",
    "last_updated": "2024-12-21T09:00:00Z"
  }
]


2. Add a New Ingredient
Route: /ingredients/
Method: POST
Description: Adds a new ingredient to the database

{
  "name": "Cocoa Powder",
  "quantity": 1.0,
  "unit": "cups"
}
Response:
{
  "_id": "60d5f483f8d4e2a5b4e5c3d3",
  "name": "Cocoa Powder",
  "quantity": 1.0,
  "unit": "cups",
  "last_updated": "2024-12-21T11:00:00Z"
}

3. Update an Existing Ingredient
Route: /ingredients/{name}
Method: PUT
Description: Updates the quantity and/or unit of an existing ingredient.
Path Parameter:

name (String): Name of the ingredient to update (e.g., "Sugar").
{
  "_id": "60d5f483f8d4e2a5b4e5c3d1",
  "name": "Sugar",
  "quantity": 3.0,
  "unit": "kg",
  "last_updated": "2024-12-22T12:00:00Z"
}

4. Delete an Ingredient
Route: /ingredients/{name}
Method: DELETE
Description: Deletes an ingredient from the database.
Path Parameter:

name (String): Name of the ingredient to delete (e.g., "Sugar").
Recipes API
1. Get All Recipes
Route: /recipes/
Method: GET
Description: Retrieves a list of all recipes stored in the database.
[
  {
    "_id": "60d5f4bdf8d4e2a5b4e5c3d2",
    "title": "Chocolate Cake",
    "ingredients": [
      {
        "name": "Flour",
        "quantity": 2,
        "unit": "cups"
      },
      {
        "name": "Sugar",
        "quantity": 1.5,
        "unit": "cups"
      },
      {
        "name": "Cocoa Powder",
        "quantity": 0.75,
        "unit": "cups"
      },
      {
        "name": "Eggs",
        "quantity": 2,
        "unit": "units"
      },
      {
        "name": "Butter",
        "quantity": 0.5,
        "unit": "cups"
      }
    ],
    "instructions": "Mix all ingredients and bake at 350°F for 30 minutes.",
    "taste": "Sweet",
    "cuisine_type": "Dessert",
    "preparation_time": 45,
    "reviews": 10,
    "created_at": "2024-12-20T09:30:00Z"
  },
  {
    "_id": "60d5f4bdf8d4e2a5b4e5c3d3",
    "title": "Spaghetti Bolognese",
    "ingredients": [
      {
        "name": "Spaghetti",
        "quantity": 200,
        "unit": "grams"
      },
      {
        "name": "Ground Beef",
        "quantity": 300,
        "unit": "grams"
      },
      {
        "name": "Tomato Sauce",
        "quantity": 2,
        "unit": "cups"
      },
      {
        "name": "Onions",
        "quantity": 1,
        "unit": "unit"
      },
      {
        "name": "Garlic",
        "quantity": 2,
        "unit": "cloves"
      }
    ],
    "instructions": "Cook spaghetti and prepare sauce with beef and vegetables.",
    "taste": "Savory",
    "cuisine_type": "Italian",
    "preparation_time": 60,
    "reviews": 8,
    "created_at": "2024-12-21T10:15:00Z"
  }
]
2. Add a New Recipe
Route: /recipes/
Method: POST
Description: Adds a new recipe to the database.
{
  "title": "Grilled Chicken Salad",
  "ingredients": [
    {
      "name": "Chicken Breast",
      "quantity": 2,
      "unit": "units"
    },
    {
      "name": "Lettuce",
      "quantity": 1,
      "unit": "head"
    },
    {
      "name": "Cherry Tomatoes",
      "quantity": 10,
      "unit": "units"
    },
    {
      "name": "Olive Oil",
      "quantity": 2,
      "unit": "tablespoons"
    },
    {
      "name": "Lemon Juice",
      "quantity": 1,
      "unit": "tablespoon"
    }
  ],
  "instructions": "Grill the chicken, chop the vegetables, and mix with olive oil and lemon juice.",
  "taste": "Savory",
  "cuisine_type": "American",
  "preparation_time": 30,
  "reviews": 5
}

