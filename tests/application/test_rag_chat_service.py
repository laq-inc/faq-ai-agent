from app.application.services.knowledge_service import KnowledgeService
from app.application.services.rag_chat_service import RAGChatService
from app.domain.entities.knowledge_chunk import KnowledgeChunk
from tests.fakes.fake_embedding_service import FakeEmbeddingService
from tests.fakes.fake_knowledge_repository import FakeKnowledgeRepository
from tests.fakes.fake_llm_service import FakeLLMService


def test_rag_chat_returns_answer_with_sources() -> None:
    embedding_service = FakeEmbeddingService()
    knowledge_repository = FakeKnowledgeRepository()
    knowledge_service = KnowledgeService(
        embedding_service,
        knowledge_repository,
    )
    llm_service = FakeLLMService()

    service = RAGChatService(
        knowledge_service=knowledge_service,
        llm_service=llm_service,
    )

    knowledge_repository.save(
        KnowledgeChunk(
            id=None,
            content="pgvectorはPostgreSQLでベクトル検索を行うための拡張機能です。",
            source="manual",
            embedding=[0.1] * 1536,
        )
    )

    answer, sources = service.chat("pgvectorとは何ですか？")

    assert answer is not None
    assert len(sources) == 1
