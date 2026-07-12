import type { KnowledgeChunk } from "@/types/knowledge";

type ChatSourcesProps = {
	knowledgeChunks: KnowledgeChunk[];
};

export function ChatSources({ knowledgeChunks }: ChatSourcesProps) {
	if (knowledgeChunks.length === 0) {
		return null;
	}

	return (
		<section className="rounded-md border border-gray-200 bg-white p-6 shadow-sm">
			<h2 className="mb-4 text-lg font-semibold text-gray-900">
				参照したナレッジ
			</h2>

			<ul className="flex flex-col gap-3">
				{knowledgeChunks.map((chunk) => (
					<li
						key={chunk.id}
						className="rounded-md border border-gray-100 bg-gray-50 p-4"
					>
						<p className="mb-2 whitespace-pre-wrap text-sm leading-6 text-gray-700">
							{chunk.content}
						</p>
						<small className="mt-2 block text-xs text-gray-500">
							出典: {chunk.source ?? "不明"}
						</small>
					</li>
				))}
			</ul>
		</section>
	);
}
