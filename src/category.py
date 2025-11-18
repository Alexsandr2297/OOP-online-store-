class Category:
    """Класс для категорий"""
    name: str  # название
    description: str  # описание
    products: list  # список товаров продуктов

    # Переменная на уровне класса для подсчета количества категорий и товаров
    count_category = 0  # количество категорий
    count_product = 0  # количество товаров

    def __init__(self, name, description, products):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.products = products
        Category.count_category += 1
        Category.count_product += len(self.products)

    def add_product(self, product):
        """Добавляет продукт в категорию и увеличивает счетчик"""
        Category.count_product += 1
        self.products.append(product)
