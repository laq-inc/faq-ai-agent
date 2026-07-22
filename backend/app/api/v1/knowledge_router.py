from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.dependencies import get_knowledge_service
from app.application.services.knowledge_service import KnowledgeService
from app.domain.exceptions.knowledge_not_found_error import KnowledgeNotFoundError
from app.schemas.knowledge_schema import (
    KnowledgeCreateRequest,
    KnowledgeResponse,
    KnowledgeSearchResponse,
    KnowledgeUpdateRequest,
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


@router.get("", response_model=list[KnowledgeResponse])
def get_all_knowledge(
    knowledge_service: KnowledgeService = Depends(get_knowledge_service),
) -> list[KnowledgeResponse]:
    results = knowledge_service.get_all_knowledge()

    return [
        KnowledgeResponse(
            id=result.id,
            content=result.content,
            source=result.source,
        )
        for result in results
    ]


@router.put("/{knowledge_id}", response_model=KnowledgeResponse)
def update_knowledge(
    knowledge_id: int,
    request: KnowledgeUpdateRequest,
    service: KnowledgeService = Depends(get_knowledge_service),
) -> KnowledgeResponse:
    try:
        knowledge = service.update_knowledge(
            knowledge_id=knowledge_id,
            content=request.content,
            source=request.source,
        )
    except KnowledgeNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc

    return KnowledgeResponse(
        id=knowledge.id,
        content=knowledge.content,
        source=knowledge.source,
    )


@router.delete("/{knowledge_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_knowledge(
    knowledge_id: int,
    service: KnowledgeService = Depends(get_knowledge_service),
) -> None:
    try:
        service.delete_knowledge(knowledge_id=knowledge_id)
    except KnowledgeNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


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
