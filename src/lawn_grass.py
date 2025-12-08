from src.product import Product


class LawnGrass(Product):
    """Класс Трава газонная"""

    country: str  # страна-производитель
    germination_period: str  # срок прорастания
    color: str  # цвет

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Метод, который инициализирует экземпляры класса."""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
