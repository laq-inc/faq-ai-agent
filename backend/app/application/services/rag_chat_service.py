from app.application.services.knowledge_service import KnowledgeService
from app.application.services.llm_service import LLMService
from app.domain.entities.knowledge_chunk import KnowledgeChunk


class RAGChatService:
    def __init__(
        self, knowledge_service: KnowledgeService, llm_service: LLMService
    ) -> None:
        self.knowledge_service = knowledge_service
        self.llm_service = llm_service

    def chat(self, question: str) -> tuple[str, list[KnowledgeChunk]]:
        knowledge_chunks = self.knowledge_service.search_knowledge(
            query=question,
            limit=3,
        )
        context = "\n\n".join([chunk.content for chunk in knowledge_chunks])
        answer = self.llm_service.generate_answer(question=question, context=context)
        return answer, knowledge_chunks
