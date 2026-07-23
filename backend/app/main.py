import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.v1.chat_router import router as chat_router
from app.api.v1.faq_router import router as faq_router
from app.api.v1.knowledge_router import router as knowledge_router
from app.infrastructure.database import engine
from app.infrastructure.models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # Fail fast at startup instead of on the first request that touches
    # OpenAI (EmbeddingService/LLMService read this lazily per-request).
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY environment variable is not set")

    with engine.begin() as conn:
        # Must run before create_all: the Vector column type requires the
        # pgvector extension to already exist in the database.
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(title="FAQ AI Agent", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(faq_router)
app.include_router(knowledge_router)
app.include_router(chat_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
