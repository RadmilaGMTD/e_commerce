def test_order_str(order1):
    """Корректная работа метода str"""
    assert str(order1).strip() == "Samsung Galaxy C23 Ultra, количество: 5 шт."


def test_order_total_price(order1):
    """Тестируем функцию, которая рассчитывает общую стоимость"""
    assert order1.total_price() == 900000.0


def test_order_get_quantity(order1):
    """Тестируем функцию, которая выводит количество продуктов"""
    assert order1.get_quantity() == 5
