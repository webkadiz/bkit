from compositor import IDietTreeComponent
from prototype import IPrototype

class Product(IDietTreeComponent, IPrototype):
    def __init__(self, params):
        self._params = params.copy()
        self._name = params.get('name')
        self._category = params.get('category')
        self._proteins = params.get('proteins')
        self._fats = params.get('fats')
        self._carbs = params.get('carbs')
        self._priceForWeight = params.get('priceForWeight')
        self._weight = params.get('weight')

    children = property(lambda self: [])

    def getPrice(self):
        return self._priceForWeight * self._weight

    def clone(self):
        return Product(self._params)