import pytest
from pydantic import ValidationError

from app.schemas.knowledge_schema import KnowledgeCreateRequest


def test_create_request_requires_source() -> None:
    with pytest.raises(ValidationError):
        KnowledgeCreateRequest(content="pgvectorとは何ですか？")


def test_create_request_rejects_empty_source() -> None:
    with pytest.raises(ValidationError):
        KnowledgeCreateRequest(content="pgvectorとは何ですか？", source="")


def test_create_request_rejects_blank_source() -> None:
    with pytest.raises(ValidationError):
        KnowledgeCreateRequest(
            content="pgvectorとは何ですか？",
            source="   ",
        )


def test_create_request_rejects_blank_content() -> None:
    with pytest.raises(ValidationError):
        KnowledgeCreateRequest(content="   ", source="manual")


def test_create_request_accepts_valid_source() -> None:
    request = KnowledgeCreateRequest(content="pgvectorとは何ですか？", source="manual")

    assert request.source == "manual"
