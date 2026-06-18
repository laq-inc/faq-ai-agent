from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.application.faq_service import FAQService
from app.infrastructure.database import get_db
from app.infrastructure.repositories.sqlalchemy_faq_repository import (
    SQLAlchemyFAQRepository,
)
from app.schemas.faq_schema import FAQCreateRequest, FAQResponse

router = APIRouter(prefix="/api/v1/faqs", tags=["faqs"])


def get_faq_service(db: Session = Depends(get_db)) -> FAQService:
    faq_repository = SQLAlchemyFAQRepository(db)
    return FAQService(faq_repository)


@router.get("", response_model=list[FAQResponse])
def get_faqs(faq_service: FAQService = Depends(get_faq_service)) -> list[FAQResponse]:
    faqs = faq_service.get_faqs()
    return [
        FAQResponse(id=faq.id, question=faq.question, answer=faq.answer) for faq in faqs
    ]


@router.post("", response_model=FAQResponse, status_code=status.HTTP_201_CREATED)
def create_faq(
    request: FAQCreateRequest, faq_service: FAQService = Depends(get_faq_service)
) -> FAQResponse:
    faq = faq_service.create_faq(request)

    return FAQResponse(id=faq.id, question=faq.question, answer=faq.answer)
