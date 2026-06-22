from app.application.services.faq_service import FAQService
from app.schemas.faq_schema import FAQCreateRequest
from tests.fakes.fake_faq_repository import FakeFAQRepository


def test_create_faqs() -> None:
    faq_repository = FakeFAQRepository()
    faq_service = FAQService(faq_repository)

    request = FAQCreateRequest(
        question="pgvectorとは何ですか？",
        answer="PostgreSQLでベクトル検索を行うための拡張機能です。",
    )

    faq = faq_service.create_faq(request)

    assert faq.id == 1
    assert faq.question == request.question
    assert faq.answer == request.answer


def test_get_faqs() -> None:
    faq_repository = FakeFAQRepository()
    faq_service = FAQService(faq_repository)

    faq_service.create_faq(
        FAQCreateRequest(
            question="RAGとは何ですか？",
            answer="検索拡張生成です。",
        )
    )

    faqs = faq_service.get_faqs()

    assert len(faqs) == 1
    assert faqs[0].question == "RAGとは何ですか？"
