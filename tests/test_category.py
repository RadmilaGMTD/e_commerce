from src.category import Category


def test_category(category, category_empty):
    """Проверка инициализации"""
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 2
    assert category_empty.products == []
    assert Category.category_count == 2
    assert Category.product_count == 2
