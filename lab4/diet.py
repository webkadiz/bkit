from compositor import IDietTreeComponent
from iterator import TreeIterator
from dish import Dish

class Diet(IDietTreeComponent):
    def __init__(self, category):
        self._category = category
        self._children = []

    children = property(lambda self: self._children)

    def addDish(self, dish):
        self.children.append(dish)

    def __iter__(self):
        return TreeIterator().depthDetour(self)

    def eatBreakfast(self, client):
        breakfast = self.getBreakfast()
        breakfast.isEated = True
        price = breakfast.getPrice()
        client.balance -= price
    
    def getBreakfast(self):
        for child in self:
            if type(child) == Dish and child.isBreakfast() and not child.isEated:
                return child


