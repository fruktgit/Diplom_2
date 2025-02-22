import pytest
import allure
from config import API_ENDPOINTS, ApiMessages

@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Логин пользователя")
class TestLoginUser:
    @allure.title("существующий пользователь может авторизоваться")
    def test_login_user_success(self, setup_and_teardown):
        self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        response = self.client.post(API_ENDPOINTS["login_user"], self.user_data)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title("не существующий пользователь не может авторизоваться")
    def test_login_incorrect_credentials(self, setup_and_teardown):
        response = self.client.post(API_ENDPOINTS["login_user"], self.user_data)
        assert response.status_code == 401 and ApiMessages.account_not_found in response.text




