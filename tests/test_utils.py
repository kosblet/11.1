import pytest
import pandas as pd
import os
from src.utils import read_csv_transactions, read_excel_transactions, read_json_file


def test_read_csv_transactions(tmp_path):
    # Создаем временный CSV файл
    csv_file = tmp_path / "test.csv"
    csv_content = (
        "1;EXECUTED;2023-09-05T10:49:52Z;25677;Peso;PHP;American Express 9868997595486172;Visa 0291209661494166;Перевод с карты на карту\n"
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
        "date": ["2023-09-05T10:49:52Z", "2023-07-22T05:02:01Z"],
        "amount": [25677, 30368],
        "currency_name": ["Peso", "Shilling"],
        "currency_code": ["PHP", "TZS"],
        "from": ["American Express 9868997595486172", "Visa 1959232722494097"],
        "to": ["Visa 0291209661494166", "Visa 6804119550473710"],
        "description": ["Перевод с карты на карту", "Перевод с карты на карту"]
    }
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False, header=False)

    # Вызываем функцию
    result = read_excel_transactions(str(excel_file))

    # Проверяем результат
    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[1]["state"] == "CANCELED"


def test_read_json_file_valid(tmp_path):
    # Создаем временный JSON файл
    json_file = tmp_path / "test.json"
    json_content = '[{"id": 1, "name": "Test"}]'
    json_file.write_text(json_content)

    # Вызываем функцию
    result = read_json_file(str(json_file))

    # Проверяем результат
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_read_json_file_empty(tmp_path):
    # Создаем пустой JSON файл
    json_file = tmp_path / "empty.json"
    json_file.write_text("")

    # Вызываем функцию
    result = read_json_file(str(json_file))

    # Проверяем результат
    assert result == []


def test_read_json_file_invalid_json(tmp_path):
    # Создаем некорректный JSON файл
    json_file = tmp_path / "invalid.json"
    json_file.write_text('{"key": "value"}')  # Не список

    # Вызываем функцию
    result = read_json_file(str(json_file))

    # Проверяем результат
    assert result == []