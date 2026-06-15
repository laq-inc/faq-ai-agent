from fastapi import FastAPI

app = FastAPI(title="RAG Agent Review App")


@app.get("/health")
def health_check():
    return {"status": "ok"}