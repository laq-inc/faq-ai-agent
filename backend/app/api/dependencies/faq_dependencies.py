from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.faq_service import FAQService
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy_faq_repository import (
    SQLAlchemyFAQRepository,
)


def get_faq_service(db: Session = Depends(get_db)) -> FAQService:
    faq_repository = SQLAlchemyFAQRepository(db)
    return FAQService(faq_repository)
