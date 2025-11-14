class Category:
    """Класс для категорий"""
    name: str  # название
    description: str  # описание
    products: list  # список товаров продуктов

    # Переменная на уровне класса для подсчета количества категорий и товаров
    number_of_categories = 0  # количество категорий
    number_of_products = 0  # количество товаров

    def __init__(self, name, description, products):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.products = products
        self.number_of_categories += 1
        self.number_of_products += len(self.products)
