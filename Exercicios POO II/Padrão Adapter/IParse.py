from abc import ABC, abstractmethod


class IParse(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def parse(self) -> dict:
        pass
