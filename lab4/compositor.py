from abc import ABC, abstractmethod

class IDietTreeComponent(ABC):
    def getPrice(self):
        price = 0

        for child in self.children:
            price += child.getPrice()

        return price

    @abstractmethod
    def children(): pass