import json
import os
from unittest.mock import mock_open, patch

from src.utils import create_objects_from_json, read_json


def test_read_json() -> None:
    """Корректное чтение файла JSON"""
    rows = [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]
    with open("../test_file.json", "w", encoding="UTF-8") as file:
        json.dump(rows, file)
    assert read_json("../test_file.json") == rows
    os.remove("../test_file.json")


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=json.dumps(
        [
            {
                "name": "Телевизоры",
                "description": "Современный телевизор",
                "products": [
                    {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
                ],
            }
        ]
    ),
)
def test_read_json_mock(mock_file: str) -> None:
    """Корректная работа функции с использованием MOCK"""
    assert read_json("../data/products.json") == [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]


def test_create_objects_from_json(data, data_empty):
    """Корректная работа функции"""
    rows = create_objects_from_json(data)
    assert rows[0].name == "Телевизоры"
    assert rows[0].description == "Современный телевизор"
    assert len(rows[0].products) == 1
    assert rows[0].products[0].name == "55 QLED 4K"
    assert rows[0].products[0].description == "Фоновая подсветка"
    assert rows[0].products[0].price == 123000.0
    assert rows[0].products[0].quantity == 7
    rows_empty = create_objects_from_json(data_empty)
    assert rows_empty == []
