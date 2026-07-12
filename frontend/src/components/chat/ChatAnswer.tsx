type ChatAnswerProps = {
	answer: string;
};

export function ChatAnswer({ answer }: ChatAnswerProps) {
	if (!answer) {
		return null;
	}

	return (
		<section className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
			<h2 className="mb-3 text-lg font-semibold text-gray-900">回答</h2>
			<p className="whitespace-pre-wrap leading-7 text-gray-700">{answer}</p>
		</section>
	);
}
