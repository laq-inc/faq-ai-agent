"use client";

import { useState } from "react";
import { ChatAnswer } from "@/components/chat/ChatAnswer";
import { ChatError } from "@/components/chat/ChatError";
import { ChatForm } from "@/components/chat/ChatForm";
import { ChatSources } from "@/components/chat/ChatSources";
import { postChat } from "@/services/chatApi";
import type { KnowledgeChunk } from "@/types/knowledge";

export default function Home() {
	const [question, setQuestion] = useState("");
	const [answer, setAnswer] = useState("");
	const [knowledgeChunks, setKnowledgeChunks] = useState<KnowledgeChunk[]>([]);
	const [isLoading, setIsLoading] = useState(false);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);

	async function handleSubmit(): Promise<void> {
		if (!question.trim()) {
			return;
		}

		setIsLoading(true);
		setAnswer("");
		setKnowledgeChunks([]);
		setErrorMessage(null);

		try {
			const response = await postChat({ question });
			setAnswer(response.answer);
			setKnowledgeChunks(response.knowledgeChunks);
		} catch {
			setErrorMessage(
				"回答の取得に失敗しました。時間をおいて再度お試しください。",
			);
		} finally {
			setIsLoading(false);
		}
	}

	return (
		<main className="mx-auto flex w-full min-h-screen max-w-4xl flex-col gap-6 p-8">
			<h1>FAQ AI Agent</h1>

			<ChatForm
				question={question}
				isLoading={isLoading}
				onQuestionChange={setQuestion}
				onSubmit={handleSubmit}
			/>

			{errorMessage && <ChatError message={errorMessage} />}

			<ChatAnswer answer={answer} />

			<ChatSources knowledgeChunks={knowledgeChunks} />
		</main>
	);
}
