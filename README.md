# e_commerce
E-commerce  — электронная торговля, или электронная коммерция.
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

## Остальные данные
* Данные представлены в файле **products.json** в директории **data**.

## Тесты
Тесты представлены для модулей **utils.py**, **product.py**, **category.py**. В проекте применяется фреймворк тестирования **pytest**. Для его использование необходимо:
1. Установить pytest:
```
poetry add --group dev pytest
```
2. Для того чтобы запустить тесты с оценкой покрытия:
```
pytest --cov
```
3. Отчет будет сгенерирован в файле с названием index.html.