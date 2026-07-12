import { z } from "zod";
import { knowledgeChunkSchema } from "@/types/knowledge";

export const chatResponseSchema = z.object({
	answer: z.string().max(500),
	knowledgeChunks: z.array(knowledgeChunkSchema),
});

export const chatRequestSchema = z.object({
	question: z.string().max(200),
});

export type ChatRequest = z.infer<typeof chatRequestSchema>;
export type ChatResponse = z.infer<typeof chatResponseSchema>;
