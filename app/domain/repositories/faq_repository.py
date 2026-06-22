from abc import ABC, abstractmethod

from app.domain.entities.faq import FAQ


class FAQRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[FAQ]:
        pass

    @abstractmethod
    def save(self, faq: FAQ) -> FAQ:
        pass
