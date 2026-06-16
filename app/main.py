from fastapi import FastAPI

from app.api.v1.faq_router import router as faq_router

app = FastAPI(title="FAQ AI Agent")

app.include_router(faq_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
