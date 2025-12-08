# OOP Online Store 🛒

Проект интернет-магазина с использованием объектно-ориентированного программирования (ООП) на Python.

## 📁 Структура проекта

src/
├── product.py # Базовый класс Product
├── smartphone.py # Класс Smartphone (наследник Product)
├── lawn_grass.py # Класс LawnGrass (наследник Product)
├── category.py # Класс Category для управления товарами
tests/
├── test_product.py # Тесты для Product
├── test_smartphone.py # Тесты для Smartphone
├── test_lawn_grass.py # Тесты для LawnGrass
├── test_category.py # Тесты для Category
README.md # Документация проекта

text

## 🚀 Функциональность

### Задание 1: Наследование и специализированные классы

Созданы два класса-наследника от базового класса `Product`:

#### **Smartphone** (Смартфон)

```python
class Smartphone(Product):
    def __init__(self, name, description, price, quantity, 
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model            # модель
        self.memory = memory          # объем памяти (ГБ)
        self.color = color            # цвет
LawnGrass (Трава газонная)
python
class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country           # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color               # цвет
Ключевые концепции: #наследование #создание_класса #init

Задание 2: Безопасное сложение товаров
Реализована проверка типов при сложении товаров:

python    
def __add__(self, other):
        """Сложение двух продуктов по цене и количеству, если оба продукта одного класса"""
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError(f"Нельзя складывать продукты разных классов: {type(self).__name__} и {type(other).__name__}")



Задание 3: Защищенное добавление товаров в категорию
Доработан метод добавления товаров в категорию с проверкой типа:

python    
def add_product(self, product):
        """Добавляет продукт в категорию и увеличивает счетчик"""
        if isinstance(product, Product):
            Category.product_count += 1
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять только экземпляры класса Product")
Ключевые концепции: #isinstance #issubclass

Задание 4: Тестирование
Написаны тесты для проверки всей функциональности:

python
# Пример теста для сложения
def test__add__():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert product1 + product2 == 2580000.0
    assert product1 + product3 == 1334000.0
    assert product2 + product3 == 2114000.0

    # Тест ошибок
    with pytest.raises(TypeError):
        product1 + 100

# Пример теста для ошибок
def test_add_product_error(category):
    with pytest.raises(TypeError) as f:
        category.add_product(123)

    # Проверяем сообщение об ошибке
    assert "Можно добавлять только экземпляры класса Product" in str(f.value)
