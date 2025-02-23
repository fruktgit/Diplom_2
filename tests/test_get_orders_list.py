import pytest
import allure
from config import API_ENDPOINTS, Ingredients, ApiMessages


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Получение доступных заказов по пользователю")
class TestGeOrders:

    @allure.title("олучение доступных заказов авторизованного пользователя")
    def test_get_order_list(self, setup_and_teardown):
        response = self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        token = response.json()["accessToken"]
        requests_create_order = self.client.post(API_ENDPOINTS["create_order"], Ingredients.correct_ingredients_data, token)
        response_get_order = self.client.get(API_ENDPOINTS["create_order"], Ingredients.correct_ingredients_data, headers=token)
        assert response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == \
               requests_create_order.json()['order']['number']

    @allure.title("Получение заказов пользователя если пользователь не авторизовался")
    def test_get_order_user_not_auth(self):
        response = self.client.get(API_ENDPOINTS["create_order"], Ingredients.correct_ingredients_data)
        assert response.status_code == 401 and ApiMessages.not_authorised in response.text
