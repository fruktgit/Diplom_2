import pytest
import allure
from utils.data_generator import generate_user_data
from config import API_ENDPOINTS, ApiMessages

@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Создание нового пользователя")
class TestCreateUser:
    @allure.title("создать уникального пользователя")
    def test_create_user_success(self, setup_and_teardown):
        response = self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_user_duplicate(self, setup_and_teardown):
        with allure.step("Первый запрос успешен"):
            self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        with allure.step("Второй запрос с дублирующими данными должен вернуть ошибку"):
            response = self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        assert response.status_code == 403 and ApiMessages.account_name_already_exists in response.json()["message"]

    @allure.title("создать пользователя и не заполнить одно из обязательных полей")
    @pytest.mark.parametrize("missing_field", [
        ("email"),
        ("password"),
        ("name")
    ])
    def test_create_user_missing_fields(self, setup_and_teardown, missing_field):
        user_data = generate_user_data()
        user_data[missing_field] = ""  # Удаляем указанное поле
        # Отправляем запрос
        response = self.client.post(API_ENDPOINTS["create_user"], user_data)
        # Проверки
        assert response.status_code == 403 and ApiMessages.missing_fields in response.text
