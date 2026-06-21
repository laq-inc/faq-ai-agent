from pydantic import BaseModel, Field


class KnowledgeCreateRequest(BaseModel):
    content: str = Field(min_length=1)
    source: str | None = None


class KnowledgeResponse(BaseModel):
    id: int
    content: str
    source: str | None = None


class KnowledgeSearchResponse(BaseModel):
    id: int
    content: str
    source: str | None = None
