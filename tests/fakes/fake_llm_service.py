class FakeLLMService:
    def generate_answer(self, question: str, context: str) -> str:
        # This is a fake implementation that returns a canned response.
        return "pgvectorとは、PostgreSQLでベクトル検索を行うための拡張機能です。"
