import type { KnowledgeChunk } from "@/types/knowledge";

type KnowledgeListProps = {
	knowledgeList: KnowledgeChunk[];
	isLoading: boolean;
	errorMessage: string | null;
	onEdit: (knowledge: KnowledgeChunk) => void;
	onDelete: (knowledge: KnowledgeChunk) => void;
	deletingKnowledgeId: number | null;
};

export function KnowledgeList({
	knowledgeList,
	isLoading,
	errorMessage,
	onEdit,
	onDelete,
	deletingKnowledgeId,
}: KnowledgeListProps) {
	if (isLoading) {
		return (
			<p className="text-sm text-slate-600" role="status">
				Knowledgeを読み込んでいます...
			</p>
		);
	}

	if (errorMessage) {
		return (
			<p className="text-sm text-red-600" role="alert">
				{errorMessage}
			</p>
		);
	}

	if (knowledgeList.length === 0) {
		return (
			<p className="text-sm text-slate-600">
				Knowledgeはまだ登録されていません。
			</p>
		);
	}

	return (
		<div className="space-y-4">
			{knowledgeList.map((knowledge) => (
				<article
					key={knowledge.id}
					className="rounded-lg border border-slate-200 bg-white p-5 shadow-sm"
				>
					<p className="text-sm font-medium text-blue-600">
						{knowledge.source}
					</p>

					<p className="mt-2 whitespace-pre-wrap text-slate-700">
						{knowledge.content}
					</p>
					<div className="mt-4 flex justify-end space-x-2">
						<button
							type="button"
							onClick={() => onEdit(knowledge)}
							className="rounded bg-blue-600 px-3 py-2 text-sm font-medium text-white hover:bg-blue-700 disabled:bg-blue-300"
							disabled={deletingKnowledgeId !== null}
						>
							編集
						</button>
						<button
							type="button"
							onClick={() => onDelete(knowledge)}
							className="rounded bg-red-600 px-3 py-2 text-sm font-medium text-white hover:bg-red-700 disabled:bg-red-300"
							disabled={deletingKnowledgeId === knowledge.id}
						>
							{deletingKnowledgeId === knowledge.id ? "削除中..." : "削除"}
						</button>
					</div>
				</article>
			))}
		</div>
	);
}
