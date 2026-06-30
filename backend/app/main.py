from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.v1.chat_router import router as chat_router
from app.api.v1.faq_router import router as faq_router
from app.api.v1.knowledge_router import router as knowledge_router
from app.infrastructure.database import engine
from app.infrastructure.models.base import Base

app = FastAPI(title="FAQ AI Agent")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(faq_router)
app.include_router(knowledge_router)
app.include_router(chat_router)


@app.on_event("startup")
def on_startup() -> None:
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
