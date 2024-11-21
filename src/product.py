class Product:
    """Класс для описания продукта"""

    name: str
    description: str
    price: float
    quantity: int
    product_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Маг.метод для строкового отображения"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Маг.метод для складывания продуктов"""
        if type(other) is self.__class__:
            result = self.__price * self.quantity + other.price * other.quantity
            return result
        raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict):
        """Класс-метод для добавления нового продукта"""
        new_product_cls = cls(**product_dict)
        for product in cls.product_list:
            if product.name == new_product_cls.name:
                product.quantity += new_product_cls.quantity
                if product.price != new_product_cls.price:
                    product.price = max(product.price, new_product_cls.price)
                return product
        cls.product_list.append(new_product_cls)
        return new_product_cls

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        """Проверка и изменение цены"""
        if new_price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная, оставляем старую цену {self.__price}")
        if self.__price > new_price > 0:
            user_input = input("Новая цена меньше. Согласны понизить цену? (y/n): ")
            if user_input.lower() == "y":
                self.__price = new_price
                print(f"Цена изменена на {self.__price}")
                return
            else:
                print(f"Цена не изменена. Оставляем старую цену {self.__price}")
                return
        elif self.__price < new_price > 0:
            self.__price = new_price
            print(f"Новая цена выше. Цена изменена на {self.__price}")
