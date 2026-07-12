from pgvector.sqlalchemy import Vector
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.models.base import Base


class KnowledgeChunkModel(Base):
    __tablename__ = "knowledge_chunks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    # 1536 matches the dimension of EmbeddingService's default model
    # (text-embedding-3-small). Changing OPENAI_EMBEDDING_MODEL to a model
    # with a different output dimension requires updating this value too.
    embedding: Mapped[list[float]] = mapped_column(Vector(1536), nullable=False)
