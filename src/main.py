from src.category import Category
from src.product import Product


def main():
    prod = Product('Samsung Galaxy C25 Ultra',
                   'Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                   'функций для удобства жизни',
                   54.980, 3)

    print(f"Название: {prod.name}")
    print(f"Описание: {prod.description}")
    print(f"Цена: {prod.price}")
    print(f"Количество: {prod.quantity}")

    print()

    cat = Category('Смартфоны', '256GB, Серый цвет, 200MP камера',
                   [Product('Samsung Galaxy C25 Ultra',
                            'Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                            'функций для удобства жизни', 54980, 5),
                    Product('Iphone 16', '512GB, Gray space', 49.000, 5),
                    Product('Xiaomi Redmi Note 15', '1024GB, Синий', 48.000, 5)])

    print(f"Категория: {cat.name}")
    print(f"Описание: {cat.description}")
    print(f"список товаров продуктов: {len(cat.products)}")
    print(f"количество категорий: {Category.count_category}")
    print(f"количество товаров: {Category.count_product}")


if __name__ == "__main__":
    main()
