# app/chatbot/chain.py
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings

from .text_spitter import split_text
from .embedding import generate_embeddings
from .store import initialize_vector_store

from .load_text_file import load_local_text_file

from .llm import llm
from pathlib import Path


# Initialize the pipeline
def initialize_rag_chain():
    # Load and process documents
    file_path = Path("E:/kuet_hackathon/kitchen_buddy/app/data/fav_food.txt")
    text = load_local_text_file(file_path)
    splits = split_text(text, chunk_size=1000, chunk_overlap=200)
    embeddings = generate_embeddings(splits)
    vectorstore = initialize_vector_store(splits, embeddings)
    retriever = vectorstore.as_retriever()
    
    # Define prompt
    prompt = hub.pull("rlm/rag-prompt")
    
    # Define post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    # Define the RAG Chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain

rag_chain = initialize_rag_chain()
