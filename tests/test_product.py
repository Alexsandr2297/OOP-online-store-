import pytest

from src.product import Product


@pytest.fixture()
def product():
    return Product('Samsung Galaxy C25 Ultra',
                   'Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                   'функций для удобства жизни',
                   54.980, 3)


def test_init(product):
    assert product.name == 'Samsung Galaxy C25 Ultra'
    assert product.description == ('Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                                   'функций для удобства жизни')
    assert product.price == 54.980
    assert product.quantity == 3
