import pytest


def test_iter_products(category_for_iter):
    """Корректная работа итератора для вывода продуктов"""
    iter(category_for_iter)
    assert category_for_iter.index == 0
    assert str(next(category_for_iter)) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(next(category_for_iter)) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    with pytest.raises(StopIteration):
        next(category_for_iter)
