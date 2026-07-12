from pydantic import BaseModel, Field, field_validator


class KnowledgeCreateRequest(BaseModel):
    content: str = Field(min_length=1)
    source: str = Field(min_length=1)

    @field_validator("content", "source")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("must not be blank")
        return v


class KnowledgeResponse(BaseModel):
    id: int
    content: str
    source: str


class KnowledgeSearchResponse(BaseModel):
    id: int
    content: str
    source: str
