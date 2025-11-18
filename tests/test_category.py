import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def category():
    products = [Product('Samsung Galaxy C25 Ultra',
                        'Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                        'функций для удобства жизни', 54980, 5),
                Product('Iphone 16', '512GB, Gray space', 49.000, 5),
                Product('Xiaomi Redmi Note 15', '1024GB, Синий', 48.000, 5)]
    return Category('Смартфоны', '256GB, Серый цвет, 200MP камера', products)


def test_init(category):
    assert category.name == 'Смартфоны'
    assert category.description == '256GB, Серый цвет, 200MP камера'
    assert len(category.products) == 3
    assert category.count_category == 1
    assert category.count_product == 3


def test_add_product(category):
    count = len(category.products)  # = 3
    total = Category.count_product  # = 3

    new_product = Product('Honor', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                        'функций для удобства жизни', 26699, 1)
    category.add_product(new_product)
    assert len(category.products) == count + 1  # = 4
    assert category.products[-1] == new_product
    assert Category.count_product == total + 1  # = 4
