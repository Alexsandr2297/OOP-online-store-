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

    def __add__(self, other):
        """Складывает общую стоимость двух упаковок газонной травы."""
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Можно складывать только экземпляры класса LawnGrass")
