from abc import ABC, abstractmethod

class IPrototype(ABC):
    @abstractmethod
    def clone(): pass