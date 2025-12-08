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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_info, product_list):
        """Создает новый товар или обновляет существующий."""

        name = product_info.get('name')
        description = product_info.get('description')
        price = product_info.get('price')
        quantity = product_info.get('quantity')

        for product in product_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        return cls(name, description,
                   price, quantity)

    @property
    def price(self):
        """Получает цену товара."""

        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену товара с проверками."""

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            confirmation = input("Цена понижается. Вы уверены? (y/n): ")
            if confirmation.lower() != 'y':
                print("Изменение цены отменено.")
                return
        self.__price = new_price

    def __str__(self):
        """Возвращает строковое представление продукта."""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}шт."

    def __add__(self, other):
        """Сложение двух продуктов по цене и количеству, если оба продукта одного класса"""

        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError(f"Нельзя складывать продукты разных классов: {type(self).__name__} и {type(other).__name__}")
