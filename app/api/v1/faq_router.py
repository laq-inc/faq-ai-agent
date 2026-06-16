from fastapi import APIRouter, status

from app.application.faq_service import FAQService
from app.schemas.faq_schema import FAQCreateRequest, FAQResponse

router = APIRouter(prefix="/api/v1/faqs", tags=["faqs"])

faq_service = FAQService()


@router.get("", response_model=list[FAQResponse])
def list_faqs() -> list[FAQResponse]:
    faqs = faq_service.list_faqs()
    return [
        FAQResponse(id=faq.id, question=faq.question, answer=faq.answer) for faq in faqs
    ]


@router.post("", response_model=FAQResponse, status_code=status.HTTP_201_CREATED)
def create_faq(request: FAQCreateRequest) -> FAQResponse:
    faq = faq_service.create_faq(request)
    return FAQResponse(id=faq.id, question=faq.question, answer=faq.answer)
