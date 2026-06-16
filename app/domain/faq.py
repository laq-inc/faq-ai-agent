from dataclasses import dataclass


@dataclass(frozen=True)
class FAQ:
    id: int
    question: str
    answer: str