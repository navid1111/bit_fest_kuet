# app/data_processing/embedding.py
from langchain_huggingface import HuggingFaceEmbeddings

def generate_embeddings(documents: list):
    """
    Generates embeddings for the given documents.
    """
    embeddings = HuggingFaceEmbeddings()
    return embeddings.embed_documents([doc.page_content for doc in documents])
