import pytest
import allure
from utils.data_generator import generate_user_data
from config import API_ENDPOINTS, ApiMessages

@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Создание нового пользователя")
class TestCreateUser:
    @allure.title("создать уникального пользователя")
    def test_create_user_success(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения

        response = client.post(API_ENDPOINTS["create_user"], user_data)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_user_duplicate(self, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения

        with allure.step("Первый запрос успешен"):
            client.post(API_ENDPOINTS["create_user"], user_data)
        with allure.step("Второй запрос с дублирующими данными должен вернуть ошибку"):
            response = client.post(API_ENDPOINTS["create_user"], user_data)
        assert response.status_code == 403 and ApiMessages.account_name_already_exists in response.json()["message"]

    @allure.title("создать пользователя и не заполнить одно из обязательных полей")
    @pytest.mark.parametrize("missing_field", [
        ("email"),
        ("password"),
        ("name")
    ])
    def test_create_user_missing_fields(self, setup_and_teardown, missing_field):
        client, user_data = setup_and_teardown  # Распаковываем значения

        user_data = generate_user_data()
        user_data[missing_field] = ""  # Удаляем указанное поле
        # Отправляем запрос
        response = client.post(API_ENDPOINTS["create_user"], user_data)
        # Проверки
        assert response.status_code == 403 and ApiMessages.missing_fields in response.text
