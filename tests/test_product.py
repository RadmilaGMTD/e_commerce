from src.product import Product


def test_product(product, category) -> None:
    """Проверка инициализации"""
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product() -> None:
    """Корректная работа функции - добавление нового продукта"""
    result = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert result.name == "Samsung Galaxy S23 Ultra"
    assert result.description == "256GB, Серый цвет, 200MP камера"
    assert result.price == 180000.0
    assert result.quantity == 5
    result.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert result.price == 180000.0
    assert result.quantity == 10
    assert len(result.product_list) == 1
    result.new_product(
        {"name": "Iphone", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, "quantity": 5}
    )
    assert len(result.product_list) == 2
    result.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 200000.0,
            "quantity": 5,
        }
    )
    assert result.price == 200000.0
    assert len(result.product_list) == 2


def test_price_setter(capsys, product):
    """Корректная работа сеттера - price"""
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная, оставляем старую цену 180000.0"
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная, оставляем старую цену 180000.0"
    product.price = 200000
    message = capsys.readouterr()
    assert message.out.strip() == "Новая цена выше. Цена изменена на 200000"


def test_str_product(product):
    """Корректная работа метода str"""
    assert str(product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_products(product, product_2):
    """Корректная работа метода add"""
    assert product + product_2 == 1100000.0
