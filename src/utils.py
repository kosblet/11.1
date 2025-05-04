import json
import pandas as pd
from datetime import datetime
from pathlib import Path
import logging
from typing import List, Dict

# Настройка логгера
logger = logging.getLogger(__name__)

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "utils.log"
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список при ошибке.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Данные успешно загружены из файла.")
                return data
            logger.warning("Файл содержит данные, не являющиеся списком.")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Читает CSV-файл с транзакциями и возвращает список словарей.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с данными о транзакциях или пустой список при ошибке.
    """
    try:
        df = pd.read_csv(file_path, sep=";", header=None)
        columns = [
            "id", "state", "date", "amount", "currency_name", "currency_code",
            "from", "to", "description"
        ]
        if len(df.columns) != len(columns):
            logger.error(f"Неверное количество столбцов в CSV-файле: {len(df.columns)}")
            return []
        df.columns = columns

        # Преобразуем числовые значения в строки
        for col in ["id", "amount"]:
            df[col] = df[col].astype(str)

        transactions = df.to_dict(orient="records")
        logger.info("CSV файл успешно прочитан.")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла: {e}")
        return []


def sort_transactions_by_date(transactions: List[Dict], reverse: bool = False) -> List[Dict]:
    """
    Сортирует транзакции по дате.

    :param transactions: Список словарей с транзакциями.
    :param reverse: Если True, сортировка будет выполнена в обратном порядке (по убыванию).
    :return: Отсортированный список транзакций.
    """
    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x.get("date", "")),
        reverse=reverse
    )


def filter_transactions_by_date(transactions: List[Dict], start_date: str, end_date: str) -> List[Dict]:
    """
    Фильтрует транзакции по диапазону дат.

    :param transactions: Список словарей с транзакциями.
    :param start_date: Начальная дата в формате ISO (YYYY-MM-DDTHH:MM:SSZ).
    :param end_date: Конечная дата в формате ISO (YYYY-MM-DDTHH:MM:SSZ).
    :return: Отфильтрованный список транзакций.
    """
    try:
        start_datetime = datetime.fromisoformat(start_date)
        end_datetime = datetime.fromisoformat(end_date)
        filtered = [
            transaction for transaction in transactions
            if start_datetime <= datetime.fromisoformat(transaction.get("date", "")) <= end_datetime
        ]
        logger.info(f"Транзакции успешно отфильтрованы за период {start_date} - {end_date}.")
        return filtered
    except Exception as e:
        logger.error(f"Ошибка при фильтрации транзакций по дате: {e}")
        return []