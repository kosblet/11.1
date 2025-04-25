import logging
import pandas as pd
import json
import re
from collections import Counter
from typing import List, Dict

# Создание логгера для модуля utils
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
    """
    try:
        logger.info(f"Попытка чтения CSV-файла: {file_path}")
        df = pd.read_csv(file_path, sep=";", header=None)
        columns = [
            "id", "state", "date", "amount", "currency_name", "currency_code",
            "from", "to", "description"
        ]
        if len(df.columns) != len(columns):
            logger.error("Ошибка: Неверное количество столбцов в CSV-файле.")
            return []
        df.columns = columns
        logger.info("CSV файл успешно прочитан.")
        return df.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.
    """
    try:
        logger.info(f"Попытка чтения Excel-файла: {file_path}")
        df = pd.read_excel(file_path)
        if not isinstance(df, pd.DataFrame):
            logger.error("Ошибка: Данные не являются DataFrame.")
            return []
        logger.info("Excel файл успешно прочитан.")
        return df.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла: {e}")
        return []


def read_json_file(file_path: str) -> List[Dict]:
    """
    Считывает JSON-файл и возвращает список словарей с данными о транзакциях.
    """
    try:
        logger.info(f"Попытка чтения JSON-файла: {file_path}")
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
        logger.error(f"Ошибка декодирования JSON: {file_path}")
        return []


def search_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Поиск транзакций по описанию с использованием регулярных выражений.
    """
    logger.info(f"Выполняется поиск транзакций по строке: {search_string}")
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    result = [
        transaction for transaction in transactions
        if pattern.search(transaction.get("description", ""))
    ]
    if result:
        logger.info(f"Найдено {len(result)} транзакций.")
    else:
        logger.warning("Транзакции не найдены.")
    return result


def count_operations_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по заданным категориям.
    """
    logger.info("Выполняется подсчет операций по категориям.")
    category_counter = Counter({category: 0 for category in categories})
    for transaction in transactions:
        description = transaction.get("description", "")
        if description in categories:
            category_counter[description] += 1
    logger.info(f"Подсчет завершен: {dict(category_counter)}")
    return dict(category_counter)