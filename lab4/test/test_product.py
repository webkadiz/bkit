import pytest
from product import Product

def test_check_get_price():
    product = Product(dict(name="Картошка", weight=2, priceForWeight=30))

    res = product.getPrice()

    assert res == 60

