import type { SubmitEventHandler } from "react";

type ChatFormProps = {
	question: string;
	isLoading: boolean;
	onQuestionChange: (question: string) => void;
	onSubmit: () => void;
};

export function ChatForm({
	question,
	isLoading,
	onQuestionChange,
	onSubmit,
}: ChatFormProps) {
	const canSubmit = !isLoading && question.trim().length > 0;

	const handleSubmit: SubmitEventHandler<HTMLFormElement> = (event) => {
		event.preventDefault();

		if (!canSubmit) {
			return;
		}

		onSubmit();
	};
	return (
		<form className="flex flex-col gap-4" onSubmit={handleSubmit}>
			<label htmlFor="question">質問内容</label>
			<textarea
				id="question"
				className="w-full rounded-lg border border-gray-300 p-4 focus:border-blue-500 focus:outline-none"
				value={question}
				onChange={(event) => onQuestionChange(event.target.value)}
				onKeyDown={(event) => {
					const isSubmitShortcut =
						event.key === "Enter" && (event.ctrlKey || event.metaKey);

					if (isSubmitShortcut && canSubmit) {
						event.preventDefault();
						onSubmit();
					}
				}}
				placeholder="質問を入力してください"
				rows={4}
			/>

			<button
				type="submit"
				className="rounded-lg bg-blue-500 px-4 py-2 text-white transition hover:bg-blue-600 disabled:cursor-not-allowed disabled:bg-gray-400"
				disabled={!canSubmit}
			>
				{isLoading ? "送信中..." : "送信"}
			</button>
		</form>
	);
}
