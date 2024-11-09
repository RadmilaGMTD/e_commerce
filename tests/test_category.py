from src.category import Category


def test_category(category, category_empty):
    """Проверка инициализации"""
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(category.products_in_list) == 2
    assert category_empty.products_in_list == []
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_counters(product):
    """Проверка счётчиков"""
    categories_counter_mem = Category.category_count
    products_counter_mem = Category.product_count
    Category("for_testing", "description", [product, product, product])
    assert Category.category_count == categories_counter_mem + 1
    assert Category.product_count == products_counter_mem + 3


def test_products_property(category):
    """Корректная работа функции с выводом приватного списка"""
    assert category.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_add_product(category, product):
    """Корректная работа функции по добавлению продукта"""
    assert len(category.products_in_list) == 2
    category.add_product(product)
    assert len(category.products_in_list) == 3


# def test_add_product_(category, product):
#     assert Category.product_count == 2
#     category.add_product(product)
#     assert Category.product_count == 3
