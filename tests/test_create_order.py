import pytest
import allure
from config import API_ENDPOINTS, Ingredients, ApiMessages



@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("создание заказа")
class TestCreateOrders:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения
        response = client.post(API_ENDPOINTS["create_user"], user_data)
        token = response.json()["accessToken"]
        response = client.post(API_ENDPOINTS["create_order"], Ingredients.correct_ingredients_data, token)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_without_auth(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения
        response = client.post(API_ENDPOINTS["create_order"], Ingredients.correct_ingredients_data)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredient(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения
        response = client.post(API_ENDPOINTS["create_order"])
        assert response.status_code == 400 and ApiMessages.missing_ingredient in response.json()["message"]

    @allure.title("Создание с невалидным хешем ингредиента")
    def test_create_order_incorrect_ingredient(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения
        response = client.post(API_ENDPOINTS["create_order"], Ingredients.incorrect_ingredients_data)
        assert response.status_code == 500 and ApiMessages.server_error in response.text
