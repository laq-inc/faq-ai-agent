from pgvector.sqlalchemy import Vector
from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.models.base import Base


class KnowledgeChunkModel(Base):
    __tablename__ = "knowledge_chunks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    embedding: Mapped[list[float] | None] = mapped_column(Vector(1536), nullable=True)
