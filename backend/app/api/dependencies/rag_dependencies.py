from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.embedding_service import EmbeddingService
from app.application.services.knowledge_service import KnowledgeService
from app.application.services.llm_service import LLMService
from app.application.services.rag_chat_service import RAGChatService
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy_knowledge_chunk_repository import (
    SQLAlchemyKnowledgeChunkRepository,
)


def get_knowledge_service(db: Session = Depends(get_db)) -> KnowledgeService:
    knowledge_chunk_repository = SQLAlchemyKnowledgeChunkRepository(db)

    embedding_service = EmbeddingService()

    return KnowledgeService(
        knowledge_chunk_repository=knowledge_chunk_repository,
        embedding_service=embedding_service,
    )


def get_rag_chat_service(
    knowledge_service: KnowledgeService = Depends(get_knowledge_service),
) -> RAGChatService:
    llm_service = LLMService()

    return RAGChatService(knowledge_service=knowledge_service, llm_service=llm_service)
