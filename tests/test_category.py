import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def category():
    products = [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)]
    return Category("Смартфоны",
                    ('Смартфоны, как средство не только коммуникации, '
                     'но и получения дополнительных функций для удобства жизни'), products)


def test_init(category):
    assert category.name == 'Смартфоны'
    assert category.description == ('Смартфоны, как средство не только коммуникации, '
                                    'но и получения дополнительных функций для удобства жизни')
    assert len(category.list_prod) == 3
    assert category.category_count == 1
    assert category.product_count == 3


def test_add_product(category):
    count = len(category.list_prod)  # = 3
    total = Category.product_count  # = 3

    new_product = Product('Honor', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                                   'функций для удобства жизни', 26699, 1)
    category.add_product(new_product)
    assert len(category.list_prod) == count + 1  # = 4
    assert category.list_prod[-1] == new_product
    assert Category.product_count == total + 1  # = 4


def test_products(category):
    assert category.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                 'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')


def test__str__(category):
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_add_product_error(category):
    with pytest.raises(TypeError) as f:
        category.add_product(123)

    # Проверяем сообщение об ошибке
    assert "Можно добавлять только экземпляры класса Product" in str(f.value)
