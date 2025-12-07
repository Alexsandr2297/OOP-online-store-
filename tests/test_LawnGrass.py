import pytest

from src.LawnGrass import LawnGrass


@pytest.fixture()
def lawn_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def lawn_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


def test_init1(lawn_grass1):
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_init2(lawn_grass2):
    assert lawn_grass2.name == "Газонная трава 2"
    assert lawn_grass2.description == "Выносливая трава"
    assert lawn_grass2.price == 450.0
    assert lawn_grass2.quantity == 15
    assert lawn_grass2.country == "США"
    assert lawn_grass2.germination_period == "5 дней"
    assert lawn_grass2.color == "Темно-зеленый"


def test_add(lawn_grass1, lawn_grass2):
    assert lawn_grass1 + lawn_grass2 == 16750.0


def test_add_error(lawn_grass1):
    with pytest.raises(TypeError):
        lawn_grass1 + 1
