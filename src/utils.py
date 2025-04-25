import pandas as pd
import json
import re
from collections import Counter
from typing import List, Dict

def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.
    """
    try:
        df = pd.read_csv(file_path, sep=";", header=None)
        columns = [
            "id", "state", "date", "amount", "currency_name", "currency_code",
            "from", "to", "description"
        ]
        if len(df.columns) != len(columns):
            print("Ошибка: Неверное количество столбцов в CSV-файле.")
            return []
        df.columns = columns
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []

def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.
    """
    try:
        df = pd.read_excel(file_path)
        if not isinstance(df, pd.DataFrame):
            print("Ошибка: Данные не являются DataFrame.")
            return []
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []

def read_json_file(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            print("Ошибка: Файл содержит данные, не являющиеся списком.")
            return []
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON.")
        return []

def search_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Поиск транзакций по описанию с использованием регулярных выражений.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    result = [
        transaction for transaction in transactions
        if pattern.search(transaction.get("description", ""))
    ]
    return result

def count_operations_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по заданным категориям.
    """
    category_counter = Counter({category: 0 for category in categories})
    for transaction in transactions:
        description = transaction.get("description", "")
        if description in categories:
            category_counter[description] += 1
    return dict(category_counter)