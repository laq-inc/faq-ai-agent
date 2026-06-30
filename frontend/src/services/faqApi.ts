import { apiClient } from "@/services/apiClient";
import type { FAQ } from "@/types/faq";

export function getFAQs(): Promise<FAQ[]> {
	return apiClient<FAQ[]>("/api/v1/faqs");
}
