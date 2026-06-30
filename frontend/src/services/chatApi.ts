import { apiClient } from "@/services/apiClient";
import type { ChatRequest, ChatResponse } from "@/types/chat";

export function postChat(request: ChatRequest): Promise<ChatResponse> {
	return apiClient<ChatResponse>("/api/v1/chat", {
		method: "POST",
		body: JSON.stringify(request),
	});
}
