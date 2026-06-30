from app.domain.entities.faq import FAQ
from app.domain.repositories.faq_repository import FAQRepository
from app.schemas.faq_schema import FAQCreateRequest


class FAQService:
    def __init__(self, faq_repository: FAQRepository) -> None:
        self._faq_repository = faq_repository

    def get_faqs(self) -> list[FAQ]:
        return self._faq_repository.find_all()

    def create_faq(self, request: FAQCreateRequest) -> FAQ:
        faq = FAQ(
            id=0,
            question=request.question,
            answer=request.answer,
        )

        return self._faq_repository.save(faq)
