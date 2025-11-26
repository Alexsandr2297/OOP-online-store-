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
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            confirmation = input("Цена понижается. Вы уверены? (y/n): ")
            if confirmation.lower() != 'y':
                print("Изменение цены отменено.")
                return
        self.__price = new_price

# if __name__ == "__main__":
#     new = Product('fcdf', 'fdf', 4, 1)
#     print(new.name)
#     print(new.description)
#     print(new.price)
#     print(new.quantity)
#
#     i = Product.new_product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#
#     print(i.name)
#     print(i.description)
#     print(i.price)
#     print(i.quantity)
