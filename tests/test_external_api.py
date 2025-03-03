import os
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.external_api import get_ruble_transactions


def test_invalid_input():
    assert get_ruble_transactions("invalid") == 0  # некорректный ввод данных
    assert get_ruble_transactions(None) == 0
    assert get_ruble_transactions(123) == 0


def test_rub_transaction():  # проверка транзакций с рублями
    transaction = {"operationAmount": {"currency": {"code": "RUB"}, "amount": 100.0}}
    assert get_ruble_transactions(transaction) == 100.0


@patch("requests.get")
def test_successful_conversion(mock_get):  # проверяем корректность конвертации
    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": 1.0}}

    mock_response = Mock()
    mock_response.json = Mock(return_value={"result": 1})
    mock_get.return_value = mock_response

    result = get_ruble_transactions(transaction)
    assert result == 1

    expected_url = "https://api.apilayer.com/exchangerates_data/convert"
    expected_params = {"to": "RUB", "from": "USD", "amount": 1.0}

    # убедимся, что все было вызвано корректно
    load_dotenv()  # загружаем переменные
    api_key = os.getenv("API_KEY")

    mock_get.assert_called_once_with(expected_url, headers={"apikey": api_key}, params=expected_params)


@patch("requests.get")
def test_conversion_failure(mock_get):
    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": 1.0}}

    mock_get.side_effect = Exception("API error")  # симулируем ошибку API

    result = get_ruble_transactions(transaction)
    assert result == 0
