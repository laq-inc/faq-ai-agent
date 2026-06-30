from dataclasses import dataclass


@dataclass(frozen=True)
class KnowledgeChunk:
    id: str | None
    content: str
    source: str | None
    embedding: list[float]
