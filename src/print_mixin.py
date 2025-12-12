class PrintMixin:
    """Миксин для автоматического вывода информации при создании объектов."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self):
        """Инициализирует миксин и выводит информацию об объекте."""

        super().__init__()
        print(repr(self))

    def __repr__(self):
        """Возвращает строковое представление объекта в формате конструктора."""

        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
