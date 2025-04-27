import json
import pandas as pd
import logging
from typing import List, Dict

# Настройка логгера
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


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями или пустой список при ошибке.
    """
    try:
        # Чтение CSV файла
        df = pd.read_csv(file_path, sep=";", header=None)

        # Определение названий столбцов
        columns = [
            "id", "state", "date", "amount", "currency_name", "currency_code",
            "from", "to", "description"
        ]

        # Проверка количества столбцов
        if len(df.columns) != len(columns):
            logger.error(f"Неверное количество столбцов в CSV-файле: {len(df.columns)}")
            return []

        # Присвоение названий столбцов
        df.columns = columns

        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        logger.info("CSV файл успешно прочитан.")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями или пустой список при ошибке.
    """
    try:
        # Чтение Excel файла
        df = pd.read_excel(file_path, header=None)

        # Определение названий столбцов
        columns = [
            "id", "state", "date", "amount", "currency_name", "currency_code",
            "from", "to", "description"
        ]

        # Проверка количества столбцов
        if len(df.columns) != len(columns):
            logger.error(f"Неверное количество столбцов в Excel-файле: {len(df.columns)}")
            return []

        # Присвоение названий столбцов
        df.columns = columns

        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        logger.info("Excel файл успешно прочитан.")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла: {e}")
        return []


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список при ошибке.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("JSON файл успешно прочитан.")
                return data
            else:
                logger.error("Файл содержит данные, не являющиеся списком.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}.")
        return []