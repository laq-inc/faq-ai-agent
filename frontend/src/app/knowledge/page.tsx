"use client";

import { useCallback, useEffect, useState } from "react";
import { KnowledgeForm } from "@/components/knowledge/KnowledgeForm";
import { KnowledgeList } from "@/components/knowledge/KnowledgeList";
import { deleteKnowledge, getKnowledgeList } from "@/services/knowledgeApi";
import type { KnowledgeChunk } from "@/types/knowledge";

export default function KnowledgeManagementPage() {
	const [knowledgeList, setKnowledgeList] = useState<KnowledgeChunk[]>([]);
	const [isLoading, setIsLoading] = useState(true);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);
	const [deleteErrorMessage, setDeleteErrorMessage] = useState<string | null>(
		null,
	);
	const [editingKnowledge, setEditingKnowledge] =
		useState<KnowledgeChunk | null>(null);
	const [deletingKnowledgeId, setDeletingKnowledgeId] = useState<number | null>(
		null,
	);

	const loadKnowledgeList = useCallback(async () => {
		setIsLoading(true);
		setErrorMessage(null);

		try {
			const response = await getKnowledgeList();
			setKnowledgeList(response);
		} catch {
			setErrorMessage("Knowledgeの取得に失敗しました。");
		} finally {
			setIsLoading(false);
		}
	}, []);

	useEffect(() => {
		void loadKnowledgeList();
	}, [loadKnowledgeList]);

	const handleDelete = async (knowledge: KnowledgeChunk) => {
		if (!window.confirm("このKnowledgeを削除しますか？")) {
			return;
		}

		setDeletingKnowledgeId(knowledge.id);
		setDeleteErrorMessage(null);

		try {
			await deleteKnowledge(knowledge.id);
			if (editingKnowledge?.id === knowledge.id) {
				setEditingKnowledge(null);
			}
			await loadKnowledgeList();
		} catch {
			setDeleteErrorMessage("Knowledgeの削除に失敗しました。");
		} finally {
			setDeletingKnowledgeId(null);
		}
	};

	return (
		<main className="min-h-screen bg-slate-50 px-4 py-8 sm:px-6 lg:px-8">
			<div className="mx-auto max-w-5xl">
				<header className="mb-8">
					<p className="mb-2 text-sm font-medium text-blue-600">
						Knowledge Management
					</p>

					<h1 className="text-3xl font-bold tracking-tight text-slate-900">
						Knowledge管理
					</h1>

					<p className="mt-2 text-sm leading-6 text-slate-600">
						RAGで利用するKnowledgeの一覧確認と新規登録を行います。
					</p>
				</header>

				<section className="mb-8 rounded-lg border border-slate-200 bg-white p-6 shadow-sm">
					<h2 className="text-lg font-semibold text-slate-900">
						Knowledge管理機能
					</h2>
					{deleteErrorMessage && (
						<p className="mt-2 text-sm text-red-600" role="alert">
							{deleteErrorMessage}
						</p>
					)}
				</section>

				<section className="mb-8">
					<h2 className="mb-4 text-xl font-semibold text-slate-900">
						{editingKnowledge ? "Knowledge編集" : "Knowledge登録"}
					</h2>

					<KnowledgeForm
						editingKnowledge={editingKnowledge}
						onSuccess={loadKnowledgeList}
						onCancelEdit={() => setEditingKnowledge(null)}
					/>
				</section>

				<section className="mt-8">
					<h2 className="mb-4 text-xl font-semibold text-slate-900">
						登録済みKnowledge
					</h2>

					<KnowledgeList
						knowledgeList={knowledgeList}
						isLoading={isLoading}
						errorMessage={errorMessage}
						onEdit={setEditingKnowledge}
						onDelete={handleDelete}
						deletingKnowledgeId={deletingKnowledgeId}
					/>
				</section>
			</div>
		</main>
	);
}
