class KnowledgeNotFoundError(Exception):
    def __init__(self, knowledge_id: int) -> None:
        self.knowledge_id = knowledge_id
        super().__init__(f"Knowledge not found: {knowledge_id}")
