from src.product import Product


class Smartphone(Product):
    """Класс для описания продукта-смартфона"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        self.__price = price

    def __add__(self, other):
        """Маг.метод для складывания продуктов"""
        if type(other) is self.__class__:
            result = self.__price * self.quantity + other.price * other.quantity
            return result
        raise TypeError
