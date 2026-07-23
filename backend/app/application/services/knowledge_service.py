from app.application.services.embedding_service import EmbeddingService
from app.domain.entities.knowledge_chunk import KnowledgeChunk
from app.domain.repositories.knowledge_chunk_repository import KnowledgeChunkRepository


class KnowledgeService:
    def __init__(
        self,
        embedding_service: EmbeddingService,
        knowledge_chunk_repository: KnowledgeChunkRepository,
    ) -> None:
        self._embedding_service = embedding_service
        self._knowledge_chunk_repository = knowledge_chunk_repository

    def create_knowledge(self, content: str, source: str) -> KnowledgeChunk:
        embedding = self._embedding_service.embed_text(content)

        knowledge_chunk = KnowledgeChunk(
            id=None,
            content=content,
            source=source,
            embedding=embedding,
        )

        return self._knowledge_chunk_repository.save(knowledge_chunk)

    def get_all_knowledge(self) -> list[KnowledgeChunk]:
        return self._knowledge_chunk_repository.find_all()

    def update_knowledge(
        self,
        knowledge_id: int,
        content: str,
        source: str,
    ) -> KnowledgeChunk:
        embedding = self._embedding_service.embed_text(content)

        knowledge_chunk = KnowledgeChunk(
            id=knowledge_id, content=content, source=source, embedding=embedding
        )

        return self._knowledge_chunk_repository.update(knowledge_chunk)

    def search_knowledge(self, query: str, limit: int = 5) -> list[KnowledgeChunk]:
        query_embedding = self._embedding_service.embed_text(query)

        return self._knowledge_chunk_repository.search_similar(query_embedding, limit)

    def delete_knowledge(self, knowledge_id: int) -> None:
        self._knowledge_chunk_repository.delete(knowledge_id)
