import pytest


def test_smartphone_product(smartphone1) -> None:
    """Проверка инициализации"""
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_product_add(smartphone1, smartphone2) -> None:
    """Корректная работа метода add"""
    assert smartphone1 + smartphone2 == 2580000.0


def test_smartphone_product_add_error(smartphone1, product) -> None:
    """Ошибка метода add"""
    with pytest.raises(TypeError):
        assert smartphone1 + product
        assert smartphone1 + 1
