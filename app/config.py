# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'default_key')
MODEL_NAME = "llama-3.1-70b-versatile"
TEMPERATURE = 0
MAX_TOKENS = None
TIMEOUT = None
MAX_RETRIES = 2
