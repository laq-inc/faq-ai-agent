import { apiClient } from "@/services/apiClient";
import {
	type KnowledgeChunk,
	knowledgeChunkListSchema,
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
