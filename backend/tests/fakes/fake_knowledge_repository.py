from app.domain.entities.knowledge_chunk import KnowledgeChunk
from app.domain.repositories.knowledge_chunk_repository import (
    KnowledgeChunkRepository,
)


class FakeKnowledgeRepository(KnowledgeChunkRepository):
    def __init__(self) -> None:
        self._knowledge_chunks: list[KnowledgeChunk] = []

    def save(self, knowledge_chunk: KnowledgeChunk) -> KnowledgeChunk:
        saved_knowledge_chunk = KnowledgeChunk(
            id=len(self._knowledge_chunks) + 1,
            content=knowledge_chunk.content,
            source=knowledge_chunk.source,
            embedding=knowledge_chunk.embedding,
        )

        self._knowledge_chunks.append(saved_knowledge_chunk)

        return saved_knowledge_chunk

    def search_similar(
        self,
        embedding: list[float],
        limit: int = 5,
    ) -> list[KnowledgeChunk]:
        return self._knowledge_chunks[:limit]
