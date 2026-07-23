from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.knowledge_chunk import KnowledgeChunk
from app.domain.exceptions.knowledge_not_found_error import KnowledgeNotFoundError
from app.domain.repositories.knowledge_chunk_repository import KnowledgeChunkRepository
from app.infrastructure.models.knowledge_chunk_model import KnowledgeChunkModel


class SQLAlchemyKnowledgeChunkRepository(KnowledgeChunkRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def save(self, knowledge_chunk: KnowledgeChunk) -> KnowledgeChunk:
        knowledge_chunk_model = KnowledgeChunkModel(
            content=knowledge_chunk.content,
            source=knowledge_chunk.source,
            embedding=knowledge_chunk.embedding,
        )

        self.db.add(knowledge_chunk_model)
        self.db.commit()
        self.db.refresh(knowledge_chunk_model)

        return KnowledgeChunk(
            id=knowledge_chunk_model.id,
            content=knowledge_chunk_model.content,
            source=knowledge_chunk_model.source,
            embedding=knowledge_chunk_model.embedding,
        )

    def find_all(self) -> list[KnowledgeChunk]:
        stmt = select(KnowledgeChunkModel).order_by(KnowledgeChunkModel.id)

        models = self.db.scalars(stmt).all()

        return [
            KnowledgeChunk(
                id=model.id,
                content=model.content,
                source=model.source,
                embedding=model.embedding,
            )
            for model in models
        ]

    def update(self, knowledge_chunk: KnowledgeChunk) -> KnowledgeChunk:
        if knowledge_chunk.id is None:
            raise ValueError("KnowledgeChunk id is required")

        model = self.db.get(KnowledgeChunkModel, knowledge_chunk.id)

        if model is None:
            raise KnowledgeNotFoundError(knowledge_chunk.id)

        model.content = knowledge_chunk.content
        model.source = knowledge_chunk.source
        model.embedding = knowledge_chunk.embedding

        self.db.commit()
        self.db.refresh(model)

        return KnowledgeChunk(
            id=model.id,
            content=model.content,
            source=model.source,
            embedding=model.embedding,
        )

    def search_similar(
        self, embedding: list[float], limit: int = 5
    ) -> list[KnowledgeChunk]:
        stmt = (
            select(KnowledgeChunkModel)
            # Cosine distance, not L2/inner product: OpenAI embeddings are
            # designed to be compared by cosine similarity.
            .order_by(KnowledgeChunkModel.embedding.cosine_distance(embedding))
            .limit(limit)
        )

        models = self.db.scalars(stmt).all()

        return [
            KnowledgeChunk(
                id=model.id,
                content=model.content,
                source=model.source,
                embedding=model.embedding,
            )
            for model in models
        ]

    def delete(self, knowledge_id: int) -> None:
        model = self.db.get(KnowledgeChunkModel, knowledge_id)

        if model is None:
            raise KnowledgeNotFoundError(knowledge_id)

        self.db.delete(model)
        self.db.commit()
