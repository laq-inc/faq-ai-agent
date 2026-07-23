import { apiClient } from "@/services/apiClient";
import {
	type CreateKnowledgeChunkRequest,
	type KnowledgeChunk,
	knowledgeChunkListSchema,
	knowledgeChunkSchema,
	type UpdateKnowledgeChunkRequest,
} from "@/types/knowledge";

export function searchKnowledge(
	query: string,
	limit = 5,
): Promise<KnowledgeChunk[]> {
	return apiClient(
		`/api/v1/knowledge/search?query=${encodeURIComponent(query)}&limit=${limit}`,
		knowledgeChunkListSchema,
	);
}

export function getKnowledgeList(): Promise<KnowledgeChunk[]> {
	return apiClient("/api/v1/knowledge", knowledgeChunkListSchema);
}

export function createKnowledge(
	request: CreateKnowledgeChunkRequest,
): Promise<KnowledgeChunk> {
	return apiClient("/api/v1/knowledge", knowledgeChunkSchema, {
		method: "POST",
		body: JSON.stringify(request),
	});
}

export function updateKnowledge(
	knowledgeId: number,
	request: UpdateKnowledgeChunkRequest,
): Promise<KnowledgeChunk> {
	return apiClient(`/api/v1/knowledge/${knowledgeId}`, knowledgeChunkSchema, {
		method: "PUT",
		body: JSON.stringify(request),
	});
}

export function deleteKnowledge(knowledgeId: number): Promise<void> {
	return apiClient(`/api/v1/knowledge/${knowledgeId}`, null, {
		method: "DELETE",
	});
}
