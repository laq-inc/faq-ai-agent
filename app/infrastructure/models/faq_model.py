from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.models.base import Base


class FAQModel(Base):
    __tablename__ = "faqs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    answer: Mapped[str] = mapped_column(Text, nullable=False)
