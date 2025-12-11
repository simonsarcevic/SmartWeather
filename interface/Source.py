from abc import ABC, abstractmethod

class Source(ABC):

    @abstractmethod
    def show(self):
        pass