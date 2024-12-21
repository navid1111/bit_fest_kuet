# app/chatbot/llm.py
from langchain_groq import ChatGroq
from ..config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS, TIMEOUT, MAX_RETRIES

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    groq_api_key=GROQ_API_KEY,
    max_tokens=MAX_TOKENS,
    timeout=TIMEOUT,
    max_retries=MAX_RETRIES,
    # Add other parameters as needed
)
