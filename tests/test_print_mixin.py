from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_print_mixin_product(capsys):
    """Тестируем класс PrintMixin для product"""
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    messag = capsys.readouterr()
    assert messag.out.strip() == "Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_print_mixin_smartphone(capsys):
    """Тестируем класс PrintMixin для smartphone1"""
    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    messag = capsys.readouterr()
    assert messag.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_print_mixin_lawn_grass(capsys):
    """Тестируем класс PrintMixin для smartphone1"""
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    messag = capsys.readouterr()
    assert messag.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
