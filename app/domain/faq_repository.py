from abc import ABC, abstractmethod

from app.domain.faq import FAQ


class FAQRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[FAQ]:
        pass

    @abstractmethod
    def create(self, faq: FAQ) -> FAQ:
        pass
