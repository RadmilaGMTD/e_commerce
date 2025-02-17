# e_commerce
E-commerce — электронная торговля, или электронная коммерция.
## Установка
1. Клонируйте репозиторий:
```
https://github.com/RadmilaGMTD/e_commerce.git
```
2. Установите зависимости:
```
poetry install
```
## Основные функции
1. Класс **Product** находится в модуле **product.py**. Класс предназначен для описания продукта.
2. Класс **Category** находится в модуле **category.py**. Класс предназначен для описания категорий.
3. Функция для чтения JSON файла **read_json** располагается в модуле **utils**.
4. Функция для создания экземпляров **create_objects_from_json** располагается в модуле **utils**.
5. Класс **ProductsIteration**, с помощью которого можно перебирать товары одной категории, располагается в модуле **iter_products**.
6. Дочерний от **Product** класс **Smartphone** предназначен для описания продукта - смартфона, располагается в модуле **smartphone_product**.
7. Дочерний от **Product** класс **LawnGrass** предназначен для описания продукта - газонная трава, располагается в модуле **lawn_grass_product**.
8. Класс **Order** находится в модуле **order.py**. Класс предназначен для описания заказов.
9. Абстрактный класс **BaseProduct** для класса **Product** и абстрактный класс **BaseOrderCategory** для классов **Category** и **Order**, располагаются в модуле **base_product**.
10. Класс-миксин **PrintMixin** печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект, располагается в модуле **print_mixin**.

## Остальные данные
* Данные представлены в файле **products.json** в директории **data**.
* Для того чтобы воспроизвести все функции, можно воспользоваться модулем **main**.

## Тесты
Тесты представлены для модулей **utils**, **product**, **category**, **smartphone_product**, **lawn_grass_product**. В проекте применяется фреймворк тестирования **pytest**. Для его использование необходимо:
1. Установить pytest:
```
poetry add --group dev pytest
```
2. Для того чтобы запустить тесты с оценкой покрытия:
```
pytest --cov
```
3. Отчет будет сгенерирован в файле с названием index.html.