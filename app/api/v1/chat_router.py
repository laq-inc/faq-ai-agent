from fastapi import APIRouter, Depends

from app.api.dependencies import get_rag_chat_service
from app.application.services.rag_chat_service import RAGChatService
from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse,
    ChatSourceResponse,
)

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["chat"],
)


@router.post("", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    rag_chat_service: RAGChatService = Depends(get_rag_chat_service),
) -> ChatResponse:
    answer, sources = rag_chat_service.chat(question=request.question)
    return ChatResponse(
        answer=answer,
        sources=[
            ChatSourceResponse(
                id=source.id,
                content=source.content,
                source=source.source,
            )
            for source in sources
        ],
    )
