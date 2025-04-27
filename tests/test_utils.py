import os
import pytest
import pandas as pd
from src.utils import read_csv_transactions, read_excel_transactions


def test_read_csv_transactions(tmp_path):
    # Создаем временный CSV файл
    csv_file = tmp_path / "test.csv"
    csv_content = (
        "1;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
        "2;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту"
    )
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write(csv_content)

    # Вызываем функцию
    result = read_csv_transactions(str(csv_file))

    # Проверяем результат
    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[1]["state"] == "CANCELED"


def test_read_excel_transactions(tmp_path):
    # Создаем временный Excel файл
    excel_file = tmp_path / "test.xlsx"
    data = {
        "id": [1, 2],
        "state": ["EXECUTED", "CANCELED"],
        "date": ["2023-09-05T11:30:32Z", "2023-07-22T05:02:01Z"],
        "amount": [16210, 30368],
        "currency_name": ["Sol", "Shilling"],
        "currency_code": ["PEN", "TZS"],
        "from": ["Счет 58803664561298323391", "Visa 1959232722494097"],
        "to": ["Счет 39745660563456619397", "Visa 6804119550473710"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False, header=False)

    # Вызываем функцию
    result = read_excel_transactions(str(excel_file))

    # Проверяем результат
    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[1]["state"] == "CANCELED"