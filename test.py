import pytest
from main import get_github_user

def test_get_github_user(mocker):
    """
    Тестируем функцию get_github_user с использованием мока для requests.get.
    """
    # Мокаем requests.get
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'johndoe',
        'name': 'John Doe',
        'public_repos': 5
    }

    # Вызываем функцию get_github_user
    result = get_github_user('johndoe')

    # Проверяем, что результат соответствует ожидаемому
    assert result == {
        'login': 'johndoe',
        'name': 'John Doe',
        'public_repos': 5
    }

def test_get_github_user_with_error(mocker):
    """
    Тестируем функцию get_github_user с использованием мока для requests.get, возвращающего ошибку.
    """
    # Мокаем requests.get
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500

    # Вызываем функцию get_github_user
    result = get_github_user('cat')

    # Проверяем, что результат соответствует ожидаемому
    assert result is None