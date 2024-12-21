# app/chatbot/prompts.py
from langchain.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are a helpful assistant that provides information based on the context below.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
)
