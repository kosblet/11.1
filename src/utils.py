import requests
import logging
from typing import Optional

# Настройка логгера для модуля utils
logger = logging.getLogger("utils_logger")
logger.setLevel(logging.DEBUG)

# Настройка file_handler
file_handler = logging.FileHandler("utils.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка форматтера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

# Константа для API ключа (замените на ваш ключ)
API_KEY = "YOUR_API_KEY"  # Замените на реальный API ключ
BASE_URL = "https://v6.exchangerate-api.com/v6"


def convert_currency(amount: float, from_currency: str, to_currency: str) -> Optional[float]:
    """
    Конвертирует сумму из одной валюты в другую с использованием API.

    :param amount: Сумма для конвертации.
    :param from_currency: Исходная валюта (например, "USD").
    :param to_currency: Целевая валюта (например, "RUB").
    :return: Конвертированная сумма или None в случае ошибки.
    """
    try:
        logger.info(f"Попытка конвертации {amount} {from_currency} в {to_currency}.")

        # Формируем URL для запроса
        url = f"{BASE_URL}/{API_KEY}/pair/{from_currency}/{to_currency}"

        # Выполняем запрос к API
        response = requests.get(url)
        data = response.json()

        # Проверяем успешность запроса
        if data.get("result") == "success":
            rate = data["conversion_rate"]
            converted_amount = amount * rate
            logger.info(f"Конвертация успешна. Курс: {rate}, Результат: {converted_amount}")
            return round(converted_amount, 2)
        else:
            logger.error(f"Ошибка при получении курса валют: {data.get('error-type')}")
            return None
    except Exception as e:
        logger.error(f"Произошла ошибка при конвертации валюты: {e}")
        return None