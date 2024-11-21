import pytest


def test_lawn_grass_product(grass1) -> None:
    """Проверка инициализации"""
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_smartphone_product_add(grass1, grass2) -> None:
    """Корректная работа метода add"""
    assert grass1 + grass2 == 16750.0


def test_smartphone_product_add_error(grass1, product) -> None:
    """Ошибка метода add"""
    with pytest.raises(TypeError):
        assert grass1 + product
        assert grass1 + 1
