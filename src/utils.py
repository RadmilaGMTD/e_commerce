import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Функция для чтения JSON файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    """Функция для создания экземпляров классов"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


# if __name__ == '__main__':
#     raw_data = read_json('../data/products.json')
#     print(raw_data)
#     products_data = create_objects_from_json(raw_data)
#     print(products_data)
#     print(products_data[0].products)
#     print(Category.category_count)
#     print(Category.product_count)
