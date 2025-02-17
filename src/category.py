from src.base_product import BaseOrderCategory
from src.product import Product


class Category(BaseOrderCategory):
    """Класс для описания категории"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        """Маг.метод для строкового отображения"""
        summ_product = 0
        for i in self.__products:
            summ_product += i.quantity
        return f"{self.name}, количество продуктов: {summ_product} шт.\n"

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, product: dict):
        """Функция для добавления нового продукта"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def total_price(self):
        """Функция считает общую стоимость продуктов"""
        total_summ = 0
        for product in self.__products:
            total_summ += product.price * product.quantity
        return total_summ

    def get_quantity(self):
        """Функция выводит количество продуктов"""
        return sum([product.quantity for product in self.__products])


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации,
#                          но и получения дополнительных функций для удобства жизни",
#                          [product1, product2])
#     print(category1.total_price())
#     print(category1.get_quantity())
