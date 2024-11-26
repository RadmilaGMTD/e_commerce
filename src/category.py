# from itertools import product

from src.base_product import BaseOrderCategory
from src.exception import ZeroQuantity
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
        for product_ in self.__products:
            product_str += f"{str(product_)}\n"
        return product_str

    def add_product(self, product_: Product):
        """Функция для добавления нового продукта"""
        if isinstance(product_, Product):
            try:
                if product_.quantity == 0:
                    raise ZeroQuantity("Количество продукта не должно быть равно 0")
            except ZeroQuantity as e:
                print(str(e))
            else:
                self.__products.append(product_)
                Category.product_count += 1
                print("Продукт добавлен")
            finally:
                print("Операция выполнена")
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def total_price(self):
        """Функция считает общую стоимость продуктов"""
        total_summ = 0
        for product_ in self.__products:
            total_summ += product_.price * product_.quantity
        return total_summ

    def get_quantity(self):
        """Функция выводит количество продуктов"""
        return sum([product_.quantity for product_ in self.__products])

    def middle_price(self):
        """Функция находит среднюю цену продуктов"""
        try:
            return sum(product_.price for product_ in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации,
#                          но и получения дополнительных функций для удобства жизни",
#                          [product1, product2])
#     print(category1.total_price())
#     print(category1.get_quantity())
#     print(category1.middle_price())
#     product3 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 1)
#     category1.add_product(product3)
#
#     try:
#         product4 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
#         category1.add_product(product4)
#     except ValueError:
#         try:
#             raise ZeroQuantity ("Количество продукта не должно быть равно 0")
#         except ZeroQuantity as e:
#             print(str(e))
#         finally:
#             print("Операция выполнена")
