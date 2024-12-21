# app/routers/chatbot_router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from ..chatbot.chain import rag_chain

router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)

class ChatRequest(BaseModel):
    user_input: str
    available_ingredients: List[str]

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
def interact_with_chatbot(request: ChatRequest):
    try:
        # Combine available ingredients into a context string
        context = ", ".join(request.available_ingredients)
        # Construct the prompt
        question = request.user_input
        # Invoke the RAG chain
        response = rag_chain.invoke({"context": context, "question": question})
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
