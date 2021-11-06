from compositor import IDietTreeComponent

class Dish(IDietTreeComponent):
    def __init__(self, category):
        self._children = []
        self._category = category
        self._isEated = False

    children = property(lambda self: self._children)

    isEated = property(lambda self: self._isEated, lambda self, val: setattr(self, '_isEated', val))

    def isBreakfast(self):
        return self._category == 'breakfast'

    def addProduct(self, product):
        self._children.append(product)
        return self