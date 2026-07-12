import { apiClient } from "@/services/apiClient";
import {
	type ChatRequest,
	type ChatResponse,
	chatResponseSchema,
} from "@/types/chat";

export function postChat(request: ChatRequest): Promise<ChatResponse> {
	return apiClient("/api/v1/chat", chatResponseSchema, {
		method: "POST",
		body: JSON.stringify(request),
	});
}
