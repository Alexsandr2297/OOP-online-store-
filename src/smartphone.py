from src.product import Product


class Smartphone(Product):
    """Класс Смартфон"""

    efficiency: float  # производительность
    model: str  # модель
    memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод, который инициализирует экземпляры класса."""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
