import pytest
from fastapi.testclient import TestClient

from app.main import app


def test_startup_fails_fast_when_openai_api_key_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"), TestClient(app):
        pass
