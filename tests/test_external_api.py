from unittest.mock import patch

import pytest

from src.external_api import convert_currency


@patch("src.external_api.requests.get")
def test_convert_currency_rub(mock_get):
    """Проверяет конвертацию RUB (без запроса к API)."""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "RUB"}}}
    result = convert_currency(transaction)
    assert result == 100.0


@patch("src.external_api.requests.get")
def test_convert_currency_usd(mock_get):
    """Проверяет конвертацию USD через API."""
    mock_get.return_value.json.return_value = {"result": 7500.0}
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 7500.0


@patch("src.external_api.requests.get")
def test_convert_currency_api_error(mock_get):
    """Проверяет обработку ошибки API."""
    mock_get.side_effect = Exception("API error")
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    result = convert_currency(transaction)
    assert result == 100.0  # Возвращается исходная сумма
