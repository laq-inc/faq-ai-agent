from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=1)


class ChatSourceResponse(BaseModel):
    id: int
    content: str
    source: str | None = None


class ChatResponse(BaseModel):
    answer: str
    knowledgeChunks: list[ChatSourceResponse]
