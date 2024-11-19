import pytest

from src.category import Category
from src.iter_products import ProductsIteration
from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def category_empty():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [],
    )


@pytest.fixture
def data() -> list:
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [{"name": "55 QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
        }
    ]


@pytest.fixture
def data_empty() -> list:
    return []


@pytest.fixture
def product_2():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 100000.0, 2)


@pytest.fixture
def category_for_iter(category):
    return ProductsIteration(category)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
