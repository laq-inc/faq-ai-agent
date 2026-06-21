from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.embedding_service import EmbeddingService
from app.application.services.knowledge_service import KnowledgeService
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy_knowledge_chunk_repository import (
    SQLAlchemyKnowledgeChunkRepository,
)


def get_knowledge_service(db: Session = Depends(get_db)) -> KnowledgeService:
    embedding_service = EmbeddingService()

    knowledge_chunk_repository = SQLAlchemyKnowledgeChunkRepository(db)

    return KnowledgeService(
        embedding_service=embedding_service,
        knowledge_chunk_repository=knowledge_chunk_repository,
    )
