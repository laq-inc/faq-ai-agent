import { z } from "zod";

export const faqSchema = z.object({
	id: z.number().positive(),
	question: z.string().max(200),
	answer: z.string().max(500),
});

export const faqListSchema = z.array(faqSchema);
export type FAQ = z.infer<typeof faqSchema>;
