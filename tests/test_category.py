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


def test_category_counters(product):
    """Проверка счётчиков"""
    categories_counter_mem = Category.category_count
    products_counter_mem = Category.product_count
    Category("for_testing", "description", [product, product, product])
    assert Category.category_count == categories_counter_mem + 1
    assert Category.product_count == products_counter_mem + 3
