from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(): pass

    def getName(self):
        return self.name