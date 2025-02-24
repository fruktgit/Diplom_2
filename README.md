
# API-тесты для Stella Burgers

## Описание
Этот репозиторий содержит автотесты для API сервиса [Stella Burgers](https://stellarburgers.nomoreparties.site/). В связи с грядущим релизом были покрыты следующие тест-кейсы:

### 1. Создание пользователя ([tests/test_create_user.py](tests/test_create_user.py))
- Создание уникального пользователя
- Создание пользователя, который уже зарегистрирован
- Создание пользователя с незаполненным обязательным полем

### 2. Логин пользователя ([tests/test_login_user.py](tests/test_login_user.py))
- Логин под существующим пользователем
- Логин с неверным логином и паролем

### 3. Изменение данных пользователя ([tests/test_changing_user_data.py](tests/test_changing_user_data.py))
- С авторизацией
- Без авторизации

### 4. Создание заказа ([tests/test_create_order.py](tests/test_create_order.py))
- С авторизацией / Без авторизации
- С ингредиентами / Без ингредиентов
- С неверным хешем ингредиентов

### 5. Получение заказов конкретного пользователя ([tests/test_get_order_for_user.py](tests/test_get_order_for_user.py))
- Авторизованный пользователь
- Неавторизованный пользователь

## Установка и настройка окружения
Перед работой с репозиторием необходимо установить зависимости:
```shell
python3 -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
```

## Запуск тестов
Запустить все тесты:
```shell
pytest tests --alluredir=allure_results
```

Запустить конкретный тест:
```shell
pytest tests/test_create_user.py
```

Запуск тестов с определенным маркером (например, `login`):
```shell
pytest -m "login"
```

## Просмотр отчётов
Для просмотра отчётов используется **Allure Report**:
```shell
allure serve allure_results
```
Allure позволяет визуализировать результаты тестов с подробной информацией о каждом тест-кейсе.

## API документация
Подробная документация API доступна в файле [API_Stella_Burger.pdf](API_documentation/API_Stella_Burger.pdf).

