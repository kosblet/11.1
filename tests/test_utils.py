import pytest
from unittest.mock import patch
import pandas as pd  # Добавьте этот импорт
from src.utils import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv):
    """
    Тестирование чтения CSV-файла.
    """
    mock_data = pd.DataFrame(
        {
            "id": [1],
            "state": ["EXECUTED"],
            "date": ["2023-05-29T10:46:27Z"],
            "amount": [17205],
            "currency_name": ["Rupiah"],
            "currency_code": ["IDR"],
            "from": ["American Express 6824612302544616"],
            "to": ["Discover 9272851343747436"],
            "description": ["Перевод с карты на карту"],
        }
    )
    mock_read_csv.return_value = mock_data

    result = read_csv_transactions("dummy.csv")
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["state"] == "EXECUTED"


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel):
    """
    Тестирование чтения Excel-файла.
    """
    mock_data = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-05-29T10:46:27Z",
                "amount": 17205,
                "currency_name": "Rupiah",
                "currency_code": "IDR",
                "from": "American Express 6824612302544616",
                "to": "Discover 9272851343747436",
                "description": "Перевод с карты на карту",
            }
        ]
    )
    mock_read_excel.return_value = mock_data

    result = read_excel_transactions("dummy.xlsx")
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["state"] == "EXECUTED"
