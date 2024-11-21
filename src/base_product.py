from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def __add__(self, *args, **kwargs):
        pass


class BaseOrderCategory(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def __str__(self) -> str:
        """Маг.метод для строкового отображения"""
        pass

    @abstractmethod
    def total_price(self):
        """Функция считает общую стоимость продуктов"""
        pass

    @abstractmethod
    def get_quantity(self):
        """Функция выводит количество продуктов"""
        pass
