from abc import ABC, abstractmethod

from app.domain.entities.knowledge_chunk import KnowledgeChunk


class KnowledgeChunkRepository(ABC):
    @abstractmethod
    def save(self, knowledge_chunk: KnowledgeChunk) -> KnowledgeChunk:
        pass

    @abstractmethod
    def find_all(self) -> list[KnowledgeChunk]:
        pass

    @abstractmethod
    def update(self, knowledge_chunk: KnowledgeChunk) -> KnowledgeChunk:
        pass

    @abstractmethod
    def search_similar(
        self, embedding: list[float], limit: int = 5
    ) -> list[KnowledgeChunk]:
        pass

    @abstractmethod
    def delete(self, knowledge_id: int) -> None:
        pass
