from sqlalchemy.orm import Session

from app.domain.faq import FAQ
from app.domain.faq_repository import FAQRepository
from app.infrastructure.models.faq_model import FAQModel


class SQLAlchemyFAQRepository(FAQRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def find_all(self) -> list[FAQ]:
        faq_models = self.db.query(FAQModel).all()

        return [
            FAQ(
                id=faq_model.id,
                question=faq_model.question,
                answer=faq_model.answer,
            )
            for faq_model in faq_models
        ]

    def create(self, faq: FAQ) -> FAQ:
        faq_model = FAQModel(
            question=faq.question,
            answer=faq.answer,
        )

        self.db.add(faq_model)
        self.db.commit()
        self.db.refresh(faq_model)

        return FAQ(
            id=faq_model.id,
            question=faq_model.question,
            answer=faq_model.answer,
        )
