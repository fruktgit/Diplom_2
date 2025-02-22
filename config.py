
BASE_URL = ' https://stellarburgers.nomoreparties.site/api'

API_ENDPOINTS = {
    "create_user": "/auth/register",
    "login_user": "/auth/login",
    "create_order": "/orders",
    "change_user": "/auth/user"
}
class ApiMessages:
    account_name_already_exists = "User already exists"
    missing_required_registration_fields = "email or password are incorrect"
    missing_required_login_fields = "Недостаточно данных для входа"
    account_not_found = "email or password are incorrect"
    missing_fields = "Email, password and name are required fields"
    right_answer = {"ok": True}
    missing_ingredient = "Ingredient ids must be provided"
    server_error = "Internal Server Error"
    not_authorised= "You should be authorised"



class Ingredients:
    correct_ingredients_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

    incorrect_ingredients_data = {
        "ingredients": ["60d3b41abdacab0026a733c6g", "609646e4dc916e00276b2870g"]}
