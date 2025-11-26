import pytest

from src.product import Product


@pytest.fixture()
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product(product):
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    result = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}, [product])
    assert result.quantity == 10
    assert result.price == 180000.0


def test_price(monkeypatch):
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.price == 180000.0

    # Проверяем установку более высокой цены
    product.price = 190000.0
    assert product.price == 190000.0

    # Проверяем установку отрицательной цены
    product.price = -800
    assert product.price == 190000.0  # цена не изменилась

    # Понижаем цену с подтверждением 'y'
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product.price = 170000.0  # изменяем цену
    assert product.price == 170000.0, "Цена должна измениться, если подтверждение 'y'"

    # Пытаемся понизить цену с отказом 'n'
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product.price = 160000.0  # пытаемся изменить цену
    assert product.price == 170000.0, "Цена не должна изменяться, если подтверждение 'n'"
