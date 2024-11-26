# from src.product import Product
from src.base_product import BaseOrderCategory
from src.exception import ZeroQuantity


class Order(BaseOrderCategory):
    """Класс для описания заказа"""

    def __init__(self, product):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        try:
            if product.quantity > 0:
                self.product = product
                print("Товар добавлен")
            else:
                raise ZeroQuantity("Количество товара не должно быть равно 0")
        except ZeroQuantity as e:
            print(str(e))
        finally:
            print("Операция выполнена")

    def __str__(self) -> str:
        """Маг.метод для строкового отображения"""
        return f"{self.product.name}, количество: {self.product.quantity} шт.\n"

    def total_price(self):
        """Функция считает общую стоимость продуктов"""
        return self.product.price * self.product.quantity

    def get_quantity(self):
        """Функция выводит количество продуктов"""
        return self.product.quantity


# if __name__ == '__main__':
#     product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     order1 = Order(product1)
#     print(order1.total_price())
#     print(Order(product2))
#     print(order1.get_quantity())
#     try:
#         product3 = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
#     except ValueError:
#         try:
#             raise ZeroQuantity ("Количество товара не должно быть равно 0")
#         except ZeroQuantity as e:
#             print(str(e))
#         finally:
#             print("Операция выполнена")
