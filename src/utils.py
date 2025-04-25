import pandas as pd
from typing import List, Dict


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла и возвращает их в виде списка словарей.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями или пустой список при ошибке.
    """
    try:
        # Чтение CSV-файла
        df = pd.read_csv(file_path, sep=";", header=None)

        # Преобразование DataFrame в список словарей
        columns = [
            "id",
            "state",
            "date",
            "amount",
            "currency_name",
            "currency_code",
            "from",
            "to",
            "description",
        ]
        if len(df.columns) != len(columns):
            print("Ошибка: Неверное количество столбцов в CSV-файле.")
            return []

        df.columns = columns
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла и возвращает их в виде списка словарей.

    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями или пустой список при ошибке.
    """
    try:
        # Чтение Excel-файла
        df = pd.read_excel(file_path)

        # Проверка, что данные являются DataFrame
        if not isinstance(df, pd.DataFrame):
            print("Ошибка: Данные не являются DataFrame.")
            return []

        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []
