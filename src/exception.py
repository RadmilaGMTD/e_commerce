class ZeroQuantity(Exception):
    """Класс для исключения нулевого количества продукта или товара"""

    def __init__(self, massage=None):
        super().__init__(massage)
