import { apiClient } from "@/services/apiClient";
import { type FAQ, faqListSchema } from "@/types/faq";

export function getFAQs(): Promise<FAQ[]> {
	return apiClient("/api/v1/faqs", faqListSchema);
}
