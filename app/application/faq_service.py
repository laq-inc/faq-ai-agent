from app.domain.faq import FAQ
from app.schemas.faq_schema import FAQCreateRequest


class FAQService:
    def __init__(self) -> None:
        self._faqs: list[FAQ] = [
            FAQ(id=1, question="RAGとは何ですか？", answer="検索拡張機能のことです。"),
            FAQ(
                id=2,
                question="FastAPIとは何ですか？",
                answer="PythonのWeb APIフレームワークです。",
            ),
        ]

    def list_faqs(self) -> list[FAQ]:
        return self._faqs

    def create_faq(self, request: FAQCreateRequest) -> FAQ:
        faq = FAQ(
            id=len(self._faqs) + 1,
            question=request.question,
            answer=request.answer,
        )
        self._faqs.append(faq)
        return faq
