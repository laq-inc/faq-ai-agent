from fastapi import Depends

from app.api.dependencies.knowledge_dependencies import get_knowledge_service
from app.application.services.knowledge_service import KnowledgeService
from app.application.services.llm_service import LLMService
from app.application.services.rag_chat_service import RAGChatService


def get_rag_chat_service(
    knowledge_service: KnowledgeService = Depends(get_knowledge_service),
) -> RAGChatService:
    llm_service = LLMService()

    return RAGChatService(knowledge_service=knowledge_service, llm_service=llm_service)
