from pydantic import BaseModel, Field


class FAQCreateRequest(BaseModel):
    question: str = Field(..., min_length=1)
    answer: str = Field(..., min_length=1)


class FAQResponse(BaseModel):
    id: int
    question: str
    answer: str
