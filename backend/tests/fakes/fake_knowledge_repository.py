from app.domain.entities.knowledge_chunk import KnowledgeChunk
from app.domain.exceptions.knowledge_not_found_error import KnowledgeNotFoundError
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

    def find_all(self) -> list[KnowledgeChunk]:
        return list(self._knowledge_chunks)

    def update(self, knowledge_chunk: KnowledgeChunk) -> KnowledgeChunk:
        for index, current_knowledge_chunk in enumerate(self._knowledge_chunks):
            if current_knowledge_chunk.id == knowledge_chunk.id:
                self._knowledge_chunks[index] = knowledge_chunk
                return knowledge_chunk

        raise KnowledgeNotFoundError(
            knowledge_chunk.id if knowledge_chunk.id is not None else 0
        )

    def search_similar(
        self,
        embedding: list[float],
        limit: int = 5,
    ) -> list[KnowledgeChunk]:
        return self._knowledge_chunks[:limit]

    def delete(self, knowledge_id: int) -> None:
        for index, current_knowledge_chunk in enumerate(self._knowledge_chunks):
            if current_knowledge_chunk.id == knowledge_id:
                del self._knowledge_chunks[index]
                return

        raise KnowledgeNotFoundError(knowledge_id)
