from app.domain.entities.faq import FAQ
from app.domain.repositories.faq_repository import FAQRepository


class FakeFAQRepository(FAQRepository):
    def __init__(self) -> None:
        self._faqs: list[FAQ] = []

    def find_all(self) -> list[FAQ]:
        return self._faqs

    def save(self, faq: FAQ) -> FAQ:
        save_faq = FAQ(
            id=len(self._faqs) + 1,
            question=faq.question,
            answer=faq.answer,
        )
        self._faqs.append(save_faq)
        return save_faq
