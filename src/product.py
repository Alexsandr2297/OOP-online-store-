class Product:
    """Класс продукта"""
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}, {self.price} руб. (Остаток: {self.quantity} шт.)"
