# app/data_processing/text_splitter.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(documents: list, chunk_size: int = 1000, chunk_overlap: int = 200) -> list:
    """
    Splits documents into smaller chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    splits = text_splitter.split_documents(documents)
    return splits
