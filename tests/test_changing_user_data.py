import pytest
import requests
import allure
from config import API_ENDPOINTS, Ingredients, ApiMessages
from utils.data_generator import generate_user_data


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite('Изменение данных пользовователя')

class TestChangingUserData:

    @allure.description("При попытке сменить email и name у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение полей у авторизованного пользователя")
    @pytest.mark.parametrize("changing_field", [
        ("email"),
        ("password"),
        ("name")
    ])
    def test_changing_user_changing_field(self, setup_and_teardown, changing_field):
        client, user_data = setup_and_teardown  # Распаковываем значения
        response = client.post(API_ENDPOINTS["create_user"], user_data)
        token = response.json()["accessToken"]

        chang_user_data = generate_user_data()
        updated_user_data = user_data.copy()
        updated_user_data[changing_field] = chang_user_data[changing_field]

        user_data[changing_field] = chang_user_data[changing_field]
        response = client.patch(API_ENDPOINTS["change_user"], updated_user_data, token)
        assert response.status_code == 200 and response.json()["user"][changing_field] == chang_user_data[
                changing_field]

    @allure.description("При попытке сменить password у авторизованного пользователя, изменение данных происходит успешно")
    @allure.title("Успешное изменение полей у авторизованного пользователя")

    def test_changing_user_changing_field(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения
        response = client.post(API_ENDPOINTS["create_user"], user_data)
        token = response.json()["accessToken"]
        changing_field = "password"

        chang_user_data = generate_user_data()
        updated_user_data = user_data.copy()
        updated_user_data[changing_field] = chang_user_data[changing_field]

        user_data[changing_field] = chang_user_data[changing_field]
        response = client.patch(API_ENDPOINTS["change_user"], updated_user_data, token)
        assert response.status_code == 200 and response.json().get("success") is True


    @allure.title("Изменение данных пользователя без авторизацией")
    def test_changing_user_data_not_auth(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения

        response = client.patch(API_ENDPOINTS["change_user"], user_data)
        assert response.status_code == 401 and ApiMessages.not_authorised in response.text
