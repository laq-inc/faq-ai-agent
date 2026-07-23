"use client";

import { type SubmitEventHandler, useEffect, useState } from "react";
import { createKnowledge, updateKnowledge } from "@/services/knowledgeApi";
import type { KnowledgeChunk } from "@/types/knowledge";

type KnowledgeFormProps = {
	editingKnowledge: KnowledgeChunk | null;
	onSuccess: () => Promise<void>;
	onCancelEdit: () => void;
};

export function KnowledgeForm({
	editingKnowledge,
	onSuccess,
	onCancelEdit,
}: KnowledgeFormProps) {
	const [source, setSource] = useState("");
	const [content, setContent] = useState("");
	const [isSubmitting, setIsSubmitting] = useState(false);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);

	useEffect(() => {
		if (editingKnowledge) {
			setSource(editingKnowledge.source);
			setContent(editingKnowledge.content);
			setErrorMessage(null);
		}
	}, [editingKnowledge]);

	const handleSubmit: SubmitEventHandler<HTMLFormElement> = async (event) => {
		event.preventDefault();

		if (isSubmitting) {
			return;
		}

		const trimmedSource = source.trim();
		const trimmedContent = content.trim();

		if (!trimmedSource || !trimmedContent) {
			setErrorMessage("Source と Content を入力してください。");
			return;
		}

		setIsSubmitting(true);
		setErrorMessage(null);

		try {
			if (editingKnowledge) {
				await updateKnowledge(editingKnowledge.id, {
					source: trimmedSource,
					content: trimmedContent,
				});
			} else {
				await createKnowledge({
					source: trimmedSource,
					content: trimmedContent,
				});
			}
			setSource("");
			setContent("");
			await onSuccess();
			if (editingKnowledge) {
				onCancelEdit();
			}
		} catch {
			setErrorMessage(
				editingKnowledge ? "更新に失敗しました。" : "登録に失敗しました。",
			);
		} finally {
			setIsSubmitting(false);
		}
	};

	const handleCancel = () => {
		setSource("");
		setContent("");
		setErrorMessage(null);
		onCancelEdit();
	};

	return (
		<form
			className="space-y-4 rounded-lg border border-slate-200 bg-white p-5 shadow-sm"
			onSubmit={handleSubmit}
		>
			<div>
				<label
					htmlFor="knowledge-source"
					className="block text-sm font-medium text-slate-700"
				>
					Source
				</label>

				<input
					id="knowledge-source"
					type="text"
					value={source}
					onChange={(event) => setSource(event.target.value)}
					className="mt-1 w-full rounded-md border border-slate-300 px-3 py-2 text-slate-900 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
					placeholder="manual"
				/>
			</div>

			<div>
				<label
					htmlFor="knowledge-content"
					className="block text-sm font-medium text-slate-700"
				>
					Content
				</label>

				<textarea
					id="knowledge-content"
					value={content}
					onChange={(event) => setContent(event.target.value)}
					className="mt-1 min-h-40 w-full rounded-md border border-slate-300 px-3 py-2 text-slate-900 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
					placeholder="登録するKnowledgeを入力してください。"
				/>
			</div>

			{errorMessage ? (
				<p role="alert" className="text-sm text-red-600">
					{errorMessage}
				</p>
			) : null}

			<div className="flex justify-end gap-3">
				{editingKnowledge ? (
					<button
						type="button"
						onClick={handleCancel}
						className="rounded-md border border-slate-300 bg-white px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-blue-200"
					>
						キャンセル
					</button>
				) : null}

				<button
					type="submit"
					disabled={isSubmitting}
					className="rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-300 disabled:cursor-not-allowed disabled:bg-blue-400"
				>
					{editingKnowledge
						? isSubmitting
							? "更新中..."
							: "更新"
						: isSubmitting
							? "登録中..."
							: "登録"}
				</button>
			</div>
		</form>
	);
}
