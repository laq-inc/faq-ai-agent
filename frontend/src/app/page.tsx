"use client";

import { useState } from "react";
import { postChat } from "@/services/chatApi";
import type { KnowledgeChunk } from "@/types/knowledge";

export default function Home() {
	const [question, setQuestion] = useState("");
	const [answer, setAnswer] = useState("");
	const [knowledgeChunks, setKnowledgeChunks] = useState<KnowledgeChunk[]>([]);
	const [isLoading, setIsLoading] = useState(false);

	async function handleSubmit(event: React.SubmitEvent<HTMLFormElement>) {
		event.preventDefault();

		if (!question.trim()) {
			return;
		}

		setIsLoading(true);
		setAnswer("");
		setKnowledgeChunks([]);

		try {
			const response = await postChat({ question });
			setAnswer(response.answer);
			setKnowledgeChunks(response.knowledgeChunks);
		} catch {
			setAnswer("エラーが発生しました。");
		} finally {
			setIsLoading(false);
		}
	}

	return (
		<main>
			<h1>FAQ AI Agent</h1>

			<section>
				<h2>チャット</h2>

				<h2>質問</h2>

				<form onSubmit={handleSubmit}>
					<textarea
						value={question}
						onChange={(event) => setQuestion(event.target.value)}
						placeholder="質問を入力してください"
					/>

					<br />

					<button type="submit" disabled={isLoading}>
						{isLoading ? "送信中..." : "送信"}
					</button>
				</form>

				{answer && (
					<section>
						<h2>回答</h2>
						<p>{answer}</p>

						<br />

						<h2>参照したナレッジ</h2>
						<div>
							{knowledgeChunks.map((chunk) => (
								<div key={chunk.id}>
									<article>
										<p>{chunk.content}</p>
										<p>出典: {chunk.source}</p>
									</article>
								</div>
							))}
						</div>
					</section>
				)}
			</section>
		</main>
	);
}
