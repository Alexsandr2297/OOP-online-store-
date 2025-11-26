class Category:
    """Класс для категорий"""
    name: str  # название
    description: str  # описание
    products: list  # список товаров продуктов

    # Переменная на уровне класса для подсчета количества категорий и товаров
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name, description, products):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Добавляет продукт в категорию и увеличивает счетчик"""
        Category.product_count += 1
        self.__products.append(product)

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. (Остаток: {product.quantity} шт.)\n"
        return products_str

    @property
    def list_prod(self):
        return self.__products
