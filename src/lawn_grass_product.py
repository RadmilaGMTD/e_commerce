from src.product import Product


class LawnGrass(Product):
    """Класс для описания продукта-газонная трава"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        self.__price = price

    def __add__(self, other):
        """Маг.метод для складывания продуктов"""
        if type(other) is self.__class__:
            result = self.__price * self.quantity + other.price * other.quantity
            return result
        raise TypeError
