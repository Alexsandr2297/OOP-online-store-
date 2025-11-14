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
    assert category.number_of_categories == 1
    assert category.number_of_products == 3
