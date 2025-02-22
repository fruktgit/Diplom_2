import pytest

from config import API_ENDPOINTS
from utils.api_client import APIClient
from utils.data_generator import generate_user_data

import os
import json

def pytest_sessionstart(session):
    # Директория для allure-results
    results_dir = "allure-results"
    os.makedirs(results_dir, exist_ok=True)

    # 1. Генерация environment.properties
    environment_data = {
        "Browser": "Chrome",
        "Browser.Version": "112.0",
        "Platform": "Windows 10",
        "Test.Environment": "Staging",
        "Build.Version": "1.0.5"
    }

    with open(os.path.join(results_dir, "environment.properties"), "w") as env_file:
        for key, value in environment_data.items():
            env_file.write(f"{key}={value}\n")

    # 2. Генерация executor.json
    executor_data = {
        "name": "Local Machine",
        "type": "Local",
        "url": "http://localhost",
        "buildOrder": 1,
        "buildName": "Local Test Run",
        "buildUrl": None,
        "reportUrl": None
    }

    with open(os.path.join(results_dir, "executor.json"), "w") as executor_file:
        json.dump(executor_data, executor_file, indent=4)


@pytest.fixture(scope="function")
def setup_and_teardown(request):
    """
    Фикстура для подготовки данных перед тестом и их очистки после теста.
    """
    client = APIClient()
    user_data = generate_user_data()
    request.cls.client = client  # Передаём объект APIClient в тестовый класс
    request.cls.user_data = user_data  # Передаём данные пользователя в тестовый класс


    yield

    # Удаление созданного курьера после теста
    response = client.post(API_ENDPOINTS["login_user"], data={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    if response.status_code == 200:
        token = response.json()["accessToken"]
        client.delete(API_ENDPOINTS["login_user"], headers={'Authorization': f'{token}'})

