```markdown
# Mofa’s Kitchen Buddy

Mofa’s Kitchen Buddy is a backend system designed to help Mofa manage his ingredients and suggest recipes based on the items available at home. Powered by a Large Language Model (LLM), the system allows Mofa to input and update his inventory, as well as interact with a chatbot to receive tailored recipe recommendations based on his preferences.

## 📚 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
  - [Ingredients API](#ingredients-api)
    - [Get All Ingredients](#get-all-ingredients)
    - [Add a New Ingredient](#add-a-new-ingredient)
    - [Update an Existing Ingredient](#update-an-existing-ingredient)
    - [Delete an Ingredient](#delete-an-ingredient)
  - [Recipes API](#recipes-api)
    - [Get All Recipes](#get-all-recipes)
    - [Add a New Recipe](#add-a-new-recipe)
    - [Get a Specific Recipe](#get-a-specific-recipe)
  - [Chatbot API](#chatbot-api)
    - [Ask a Question](#ask-a-question)
- [Model Hosting](#model-hosting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## ✨ Features

- **Ingredient Management:** Add, update, delete, and list available ingredients.
- **Recipe Management:** Add, retrieve, and list favorite recipes.
- **Chatbot Integration:** Interact with an LLM-based chatbot to receive recipe suggestions based on available ingredients and user preferences.
- **Scalable Database:** Utilizes MongoDB for efficient storage and retrieval of ingredients and recipes.

## 🛠 Technologies Used

- **Backend Framework:** FastAPI
- **Database:** MongoDB
- **Asynchronous Driver:** Motor
- **Data Validation:** Pydantic
- **LLM Integration:** LangChain with HuggingFace Embeddings and ChatGroq
- **Deployment:** Uvicorn

## 📂 Project Structure

```
mofas-kitchen-buddy/
├── Challenge1/
│   └── analysis_notebook.ipynb
├── Challenge2/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── crud.py
│   │   ├── chatbot/
│   │   │   ├── __init__.py
│   │   │   ├── chain.py
│   │   │   └── load_text_file.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── ingredients_router.py
│   │   │   └── recipes_router.py
│   │   └── data/
│   │       └── fav_food.txt
│   ├── requirements.txt
│   └── README.md
└── README.md
```

- **Challenge1/**: Contains the Jupyter Notebook from Challenge 1.
- **Challenge2/**: Contains the backend solution with FastAPI.
  - **app/**: Main application directory.
    - **chatbot/**: Contains chatbot-related modules.
    - **routers/**: API route definitions.
    - **data/**: Stores the `fav_food.txt` file containing recipe data.
  - **requirements.txt**: Lists all Python dependencies.
- **README.md**: This documentation file.

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mofas-kitchen-buddy.git
cd mofas-kitchen-buddy/Challenge2
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv env
```

- **Windows Command Prompt:**

  ```cmd
  env\Scripts\activate
  ```

- **PowerShell:**

  ```powershell
  .\env\Scripts\Activate.ps1
  ```

- **macOS/Linux:**

  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the `Challenge2` directory and add:

```env
MONGODB_URI=mongodb://localhost:27017
GROQ_API_KEY=your_groq_api_key_here
```

*Replace `your_groq_api_key_here` with your actual Groq API key.*

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000/`.

## 🎯 Usage

Once the server is running, you can interact with the APIs using tools like **Swagger UI**, **Postman**, or **cURL**.

- **Swagger UI:** Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access interactive API documentation.

## 📝 API Documentation

### Ingredients API

#### Get All Ingredients

- **Route:** `/ingredients/`
- **Method:** `GET`
- **Description:** Retrieves a list of all available ingredients.

**Sample Response:**

```json
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
```

---

#### Add a New Ingredient

- **Route:** `/ingredients/`
- **Method:** `POST`
- **Description:** Adds a new ingredient to the database.

**Sample Payload:**

```json
{
  "name": "Cocoa Powder",
  "quantity": 1.0,
  "unit": "cups"
}
```

**Sample Response:**

```json
{
  "_id": "60d5f483f8d4e2a5b4e5c3d3",
  "name": "Cocoa Powder",
  "quantity": 1.0,
  "unit": "cups",
  "last_updated": "2024-12-21T11:00:00Z"
}
```

**Possible Error Response (Ingredient Already Exists):**

```json
{
  "detail": "Ingredient already exists."
}
```

---

#### Update an Existing Ingredient

- **Route:** `/ingredients/{name}`
- **Method:** `PUT`
- **Description:** Updates the quantity and/or unit of an existing ingredient.

**Path Parameter:**

- `name` (`String`): Name of the ingredient to update (e.g., "Sugar").

**Sample Payload:**

```json
{
  "quantity": 3.0,
  "unit": "kg"
}
```

**Sample Response:**

```json
{
  "_id": "60d5f483f8d4e2a5b4e5c3d1",
  "name": "Sugar",
  "quantity": 3.0,
  "unit": "kg",
  "last_updated": "2024-12-22T12:00:00Z"
}
```

**Possible Error Response (Ingredient Not Found):**

```json
{
  "detail": "Ingredient not found."
}
```

---

#### Delete an Ingredient

- **Route:** `/ingredients/{name}`
- **Method:** `DELETE`
- **Description:** Deletes an ingredient from the database.

**Path Parameter:**

- `name` (`String`): Name of the ingredient to delete (e.g., "Sugar").

**Sample Response:**

```json
{
  "detail": "Ingredient deleted successfully."
}
```

**Possible Error Response (Ingredient Not Found):**

```json
{
  "detail": "Ingredient not found."
}
```

---

### Recipes API

#### Get All Recipes

- **Route:** `/recipes/`
- **Method:** `GET`
- **Description:** Retrieves a list of all recipes stored in the database.

**Sample Response:**

```json
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
```

---

#### Add a New Recipe

- **Route:** `/recipes/`
- **Method:** `POST`
- **Description:** Adds a new recipe to the database.

**Sample Payload:**

```json
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
```

**Sample Response:**

```json
{
  "_id": "60d5f4bdf8d4e2a5b4e5c3d4",
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
  "reviews": 5,
  "created_at": "2024-12-22T14:45:00Z"
}
```

**Possible Error Response (Recipe Already Exists):**

```json
{
  "detail": "Recipe already exists."
}
```

---

#### Get a Specific Recipe

- **Route:** `/recipes/{title}`
- **Method:** `GET`
- **Description:** Retrieves details of a specific recipe by its title.

**Path Parameter:**

- `title` (`String`): Title of the recipe to retrieve (e.g., "Chocolate Cake").

**Sample Response:**

```json
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
}
```

**Possible Error Response (Recipe Not Found):**

```json
{
  "detail": "Recipe not found."
}
```

---

### Chatbot API

#### Ask a Question

- **Route:** `/chatbot/ask`
- **Method:** `POST`
- **Description:** Interacts with the LLM-based chatbot to suggest recipes based on user preferences and available ingredients.

**Sample Payload:**

```json
{
  "question": "I live in a flood prone region, what techniques can I use to grow rice here?"
}
```

**Sample Response:**

```json
{
  "answer": "Based on your location in a flood-prone region, you can use the following techniques to grow rice:\n1. **Floating Rice Varieties:** Utilize rice varieties that can float on water during floods.\n2. **Flood-Resistant Cropping Systems:** Implement cropping systems that can withstand periodic flooding.\n3. **Raised Bed Cultivation:** Create raised beds to protect rice plants from floodwaters.\n4. **Integrated Pest Management:** Manage pests that thrive in flooded conditions.\n5. **Drainage Systems:** Install proper drainage to control water levels during the growing season."
}
```

**Possible Error Response (Internal Server Error):**

```json
{
  "detail": "An unexpected error occurred while processing your request."
}
```

---

## 🤖 Model Hosting

The trained model for the chatbot is hosted on [Hugging Face](https://huggingface.co/your-model-link). You can access and integrate it using the provided API key.

*If you're unable to host the model on Hugging Face, you can use Git LFS to share the model files. Ensure to update the `.gitignore` accordingly to handle large files.*

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

Please ensure that your contributions adhere to the project's coding standards and include relevant tests where applicable.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

For any inquiries or support, please contact:

- **Name:** Your Name
- **Email:** your_email@example.com
- **GitHub:** [yourusername](https://github.com/yourusername)

---

## 🎉 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [LangChain](https://www.langchain.com/)
- [Hugging Face](https://huggingface.co/)
- [Uvicorn](https://www.uvicorn.org/)
```
