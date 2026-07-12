from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_faq_service
from app.application.services.faq_service import FAQService
from app.schemas.faq_schema import FAQCreateRequest, FAQResponse

router = APIRouter(prefix="/api/v1/faqs", tags=["faqs"])


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
