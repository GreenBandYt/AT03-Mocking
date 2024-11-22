import pytest

from main import get_weather


def test_get_weather(mocker):
    mock_get  = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'sunny'}],
        'main': {'temp': 25}
    }

api_key = 'dc35564d847fa8ae8e9d86110603519c'
city = 'New York'

weather_data = get_weather(api_key, city)

assert weather_data == {'weather': [{'description': 'sunny'}], 'main': {'temp': 25}}