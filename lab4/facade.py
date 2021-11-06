from diet import Diet
from dish import Dish
from product import Product


products = [
    oatgroats:= Product(dict(name="Овсяная крупа", priceForWeight=30, weight=1)),
    water:= Product(dict(name="Вода", priceForWeight=23, weight=1)),
    cabbage:= Product(dict(name="Капуста", priceForWeight=123, weight=1)),
    beet:= Product(dict(name="Свекла", priceForWeight=333, weight=1)),
    fish:= Product(dict(name="Рыба", priceForWeight=500, weight=1)),
]

class DietKeto():
    def __init__(self):
        self._diet = Diet('keto')
        self._diet.addDish(
            Dish('breakfast')
                .addProduct(oatgroats.clone())
                .addProduct(water.clone()),
        )
        self._diet.addDish(
            Dish('launch')
                .addProduct(water.clone())
                .addProduct(cabbage.clone())
                .addProduct(beet.clone()),
        )
        self._diet.addDish(
            Dish('dinner')
                .addProduct(fish.clone())
        )

    def eatBreakfast(self, client):
        self._diet.eatBreakfast(client)