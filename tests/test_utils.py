import pytest
from src.utils import (
    read_json_file,
    read_csv_transactions,
    sort_transactions_by_date,
    filter_transactions_by_date
)


def test_read_json_file_success(tmp_path):
    """
    Тест успешного чтения JSON-файла.
    """
    mock_data = '[{"id": 12345, "status": "COMPLETED"}]'
    file_path = tmp_path / "test.json"
    file_path.write_text(mock_data, encoding="utf-8")

    result = read_json_file(str(file_path))
    expected_result = [{"id": 12345, "status": "COMPLETED"}]
    assert result == expected_result


def test_read_csv_transactions(tmp_path):
    """
    Тест успешного чтения CSV-файла.
    """
    csv_content = (
        "1;EXECUTED;2023-09-05T10:49:52Z;25677;Peso;PHP;American Express 9868997595486172;Visa 0291209661494166;Перевод с карты на карту\n"
        "2;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту"
    )
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    result = read_csv_transactions(str(csv_file))
    expected_result = [
        {
            "id": "1", "state": "EXECUTED", "date": "2023-09-05T10:49:52Z",
            "amount": "25677", "currency_name": "Peso", "currency_code": "PHP",
            "from": "American Express 9868997595486172", "to": "Visa 0291209661494166",
            "description": "Перевод с карты на карту"
        },
        {
            "id": "2", "state": "CANCELED", "date": "2023-07-22T05:02:01Z",
            "amount": "30368", "currency_name": "Shilling", "currency_code": "TZS",
            "from": "Visa 1959232722494097", "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту"
        }
    ]
    assert result == expected_result


def test_sort_transactions_by_date():
    """
    Тест сортировки транзакций по дате.
    """
    transactions = [
        {"id": "1", "date": "2023-05-01T10:00:00Z"},
        {"id": "2", "date": "2023-01-01T10:00:00Z"},
        {"id": "3", "date": "2023-12-01T10:00:00Z"}
    ]
    sorted_transactions = sort_transactions_by_date(transactions)
    assert [t["id"] for t in sorted_transactions] == ["2", "1", "3"]


def test_filter_transactions_by_date():
    """
    Тест фильтрации транзакций по диапазону дат.
    """
    transactions = [
        {"id": "1", "date": "2023-05-01T10:00:00Z"},
        {"id": "2", "date": "2023-01-01T10:00:00Z"},
        {"id": "3", "date": "2023-12-01T10:00:00Z"}
    ]
    filtered = filter_transactions_by_date(transactions, "2023-02-01T00:00:00Z", "2023-11-01T00:00:00Z")
    assert [t["id"] for t in filtered] == ["1"]