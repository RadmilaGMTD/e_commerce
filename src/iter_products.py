class ProductsIteration:
    """Класс для перебора товаров одной категории"""

    def __init__(self, category_obj):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self):
        """Метод для создания итератора"""
        self.index = 0
        return self

    def __next__(self):
        """Метод для определения следующего элемента в итерации"""
        if self.index < len(self.category_obj.products_in_list):
            product = self.category_obj.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации,
#                          но и получения дополнительных функций для удобства жизни",
#                          [product1, product2, product3])
#
#     iter_products_ = ProductsIteration(category1)
#     for product_ in iter_products_:
#         print(product_)
