import pytest
from tests.fakes.fake_embedding_service import FakeEmbeddingService
from tests.fakes.fake_knowledge_repository import FakeKnowledgeRepository

from app.application.services.knowledge_service import KnowledgeService
from app.domain.exceptions.knowledge_not_found_error import KnowledgeNotFoundError


def test_delete_knowledge_success():
    # Arrange
    repo = FakeKnowledgeRepository()
    service = KnowledgeService(FakeEmbeddingService(), repo)

    knowledge = service.create_knowledge(content="test content", source="test source")
    knowledge_id = knowledge.id

    # Act
    service.delete_knowledge(knowledge_id)

    # Assert
    all_knowledge = service.get_all_knowledge()
    assert len(all_knowledge) == 0


def test_delete_knowledge_not_found():
    # Arrange
    repo = FakeKnowledgeRepository()
    service = KnowledgeService(FakeEmbeddingService(), repo)

    # Act & Assert
    with pytest.raises(KnowledgeNotFoundError, match="Knowledge not found"):
        service.delete_knowledge(999)


def test_delete_only_target_knowledge():
    # Arrange
    repo = FakeKnowledgeRepository()
    service = KnowledgeService(FakeEmbeddingService(), repo)

    k1 = service.create_knowledge(content="content 1", source="source 1")
    k2 = service.create_knowledge(content="content 2", source="source 2")

    # Act
    service.delete_knowledge(k1.id)

    # Assert
    all_knowledge = service.get_all_knowledge()
    assert len(all_knowledge) == 1
    assert all_knowledge[0].id == k2.id
