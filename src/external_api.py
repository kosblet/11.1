import os
import requests
from typing import Dict

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях (float).
    """
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = (
        transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")
    )

    # Если валюта уже в рублях, возвращаем исходную сумму
    if currency == "RUB":
        return amount

    try:
        # Запрос к API для конвертации валюты
        params = {"from": currency, "to": "RUB", "amount": amount}
        headers = {"apikey": API_KEY}
        response = requests.get(BASE_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return float(data.get("result", amount))  # Возвращаем сконвертированную сумму
    except Exception:
        return amount  # Возвращаем исходную сумму при ошибке
