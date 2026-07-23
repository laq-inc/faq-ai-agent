import os

from openai import OpenAI


class LLMService:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            timeout=float(os.getenv("OPENAI_TIMEOUT", "30.0")),
        )
        self.model = os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1-mini")

    def generate_answer(self, question: str, context: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "あなたは社内FAQに回答するAIアシスタントです。"
                        "必ず与えられたcontextの内容を根拠に回答してください。"
                        "contextに答えがない場合は、分からないと回答してください。"
                    ),
                },
                {
                    "role": "user",
                    "content": (f"context:\n{context}\n\nquestion:\n{question}"),
                },
            ],
            # Deterministic output so answers stay strictly grounded in the
            # given context, per the system prompt above.
            temperature=0,
        )
        return response.choices[0].message.content or ""
