from fastapi.testclient import TestClient
from tests.fakes.fake_embedding_service import FakeEmbeddingService
from tests.fakes.fake_knowledge_repository import FakeKnowledgeRepository

from app.api.dependencies import get_knowledge_service
from app.application.services.knowledge_service import KnowledgeService
from app.main import app


def get_test_knowledge_service():
    return KnowledgeService(FakeEmbeddingService(), FakeKnowledgeRepository())


def test_delete_knowledge_endpoint_success():
    client = TestClient(app)
    service = get_test_knowledge_service()
    app.dependency_overrides[get_knowledge_service] = lambda: service

    # Pre-populate
    k = service.create_knowledge(content="to be deleted", source="test")

    response = client.delete(f"/api/v1/knowledge/{k.id}")

    assert response.status_code == 204
    assert service.get_all_knowledge() == []

    app.dependency_overrides.clear()


def test_delete_knowledge_endpoint_not_found():
    client = TestClient(app)
    app.dependency_overrides[get_knowledge_service] = get_test_knowledge_service

    response = client.delete("/api/v1/knowledge/999")

    assert response.status_code == 404

    app.dependency_overrides.clear()
