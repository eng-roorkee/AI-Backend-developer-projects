from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse
from services.ai_service import generate_ai_reply

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatResponse):
    reply =generate_ai_reply(request.message)
    return ChatResponse(reply=reply)
