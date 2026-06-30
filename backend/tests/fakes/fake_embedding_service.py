class FakeEmbeddingService:
    def embed_text(self, text: str) -> list[float]:
        return [0.1] * 1536
