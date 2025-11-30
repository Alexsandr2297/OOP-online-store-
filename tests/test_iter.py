import pytest
from src.product import Product
from src.category import Category
from src.catagory_iterator import CategoryIterator


@pytest.fixture
def test_sampel():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3])


def test_category_iterator(test_sampel):
    iterator = CategoryIterator(test_sampel)
    products = list(iterator)
    assert products == test_sampel.list_prod
