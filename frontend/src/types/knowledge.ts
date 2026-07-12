import { z } from "zod";

export const knowledgeChunkSchema = z.object({
	id: z.number().positive(),
	content: z.string().max(500),
	source: z.string().max(200).nullable(),
});

export const knowledgeChunkListSchema = z.array(knowledgeChunkSchema);
export type KnowledgeChunk = z.infer<typeof knowledgeChunkSchema>;
