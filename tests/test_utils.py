import pytest
from unittest.mock import patch
from src.utils import convert_currency


def test_convert_currency_success():
    """
    Тест успешной конвертации валюты.
    """
    mock_response = {
        "result": "success",
        "conversion_rate": 75.0  # Пример курса USD -> RUB
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response

        result = convert_currency(100, "USD", "RUB")
        assert result == 7500.0  # 100 USD * 75 RUB/USD


def test_convert_currency_failure():
    """
    Тест неудачной конвертации валюты (ошибка API).
    """
    mock_response = {
        "result": "error",
        "error-type": "unsupported-code"
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response

        result = convert_currency(100, "XYZ", "RUB")
        assert result is None  # Ожидаем None при ошибке


def test_convert_currency_exception():
    """
    Тест обработки исключения при конвертации валюты.
    """
    with patch("requests.get") as mock_get:
        mock_get.side_effect = Exception("Network error")

        result = convert_currency(100, "USD", "RUB")
        assert result is None  # Ожидаем None при исключении