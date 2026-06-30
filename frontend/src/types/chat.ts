import type { KnowledgeChunk } from "@/types/knowledge";

export type ChatRequest = {
	question: string;
};

export type ChatResponse = {
	answer: string;
	knowledgeChunks: KnowledgeChunk[];
};
