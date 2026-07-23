import { z } from "zod";

export const knowledgeChunkSchema = z.object({
	id: z.number().positive(),
	content: z.string().min(1).max(500),
	source: z.string().min(1).max(200),
});

export const knowledgeChunkListSchema = z.array(knowledgeChunkSchema);

export type KnowledgeChunk = z.infer<typeof knowledgeChunkSchema>;

export const createKnowledgeChunkSchema = z.object({
	content: z.string().min(1).max(500),
	source: z.string().min(1).max(200),
});

export type CreateKnowledgeChunkRequest = z.infer<
	typeof createKnowledgeChunkSchema
>;

export const updateKnowledgeSchema = z.object({
	content: z.string().min(1).max(500),
	source: z.string().min(1).max(200),
});

export type UpdateKnowledgeChunkRequest = z.infer<typeof updateKnowledgeSchema>;
