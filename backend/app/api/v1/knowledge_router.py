from fastapi import APIRouter, Depends, Query, status

from app.api.dependencies import get_knowledge_service
from app.application.services.knowledge_service import KnowledgeService
from app.schemas.knowledge_schema import (
    KnowledgeCreateRequest,
    KnowledgeResponse,
    KnowledgeSearchResponse,
)

router = APIRouter(prefix="/api/v1/knowledge", tags=["knowledge"])


@router.post("", response_model=KnowledgeResponse, status_code=status.HTTP_201_CREATED)
def create_knowledge(
    request: KnowledgeCreateRequest,
    knowledge_service: KnowledgeService = Depends(get_knowledge_service),
) -> KnowledgeResponse:
    knowledge = knowledge_service.create_knowledge(
        content=request.content, source=request.source
    )

    return KnowledgeResponse(
        id=knowledge.id,
        content=knowledge.content,
        source=knowledge.source,
    )


@router.get("/search", response_model=list[KnowledgeSearchResponse])
def search_knowledge(
    query: str = Query(min_length=1),
    limit: int = Query(default=5, ge=1, le=20),
    knowledge_service: KnowledgeService = Depends(get_knowledge_service),
) -> list[KnowledgeSearchResponse]:
    results = knowledge_service.search_knowledge(query=query, limit=limit)

    return [
        KnowledgeSearchResponse(
            id=result.id,
            content=result.content,
            source=result.source,
        )
        for result in results
    ]
