from dataclasses import dataclass


@dataclass(frozen=True)
class KnowledgeChunk:
    id: int | None
    content: str
    source: str
    embedding: list[float]
