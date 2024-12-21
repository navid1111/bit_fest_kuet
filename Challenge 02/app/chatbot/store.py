# app/vector_store/store.py
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def initialize_vector_store(documents: list, embeddings: list):
    """
    Initializes the Chroma vector store with the given documents and embeddings.
    """
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=HuggingFaceEmbeddings()
    )
    return vectorstore
