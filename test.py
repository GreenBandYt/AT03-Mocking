import pytest
from main import get_weather

def test_get_weather(mocker):
    """
    Тестируем функцию get_weather с использованием мока для requests.get.
    """
    # Мокаем requests.get
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'sunny'}],
        'main': {'temp': 25}
    }

    # Вызов функции с мокированным requests.get
    api_key = 'test_api_key'
    city = 'New York'
    weather_data = get_weather(api_key, city)

    # Проверка результата
    assert weather_data == {
        'weather': [{'description': 'sunny'}],
        'main': {'temp': 25}
    }

    # Проверяем, что requests.get был вызван с правильным URL
    mock_get.assert_called_once_with(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
