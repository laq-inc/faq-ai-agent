import { apiClient } from "@/services/apiClient";
import type { KnowledgeChunk } from "@/types/knowledge";

export function searchKnowledge(query: string): Promise<KnowledgeChunk[]> {
	return apiClient<KnowledgeChunk[]>(
		`/api/v1/knowledge/search?query=${encodeURIComponent(query)}`,
	);
}
