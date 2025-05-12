import os
import sys

from src.widget import format_date

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))


def test_format_date_valid():
    result = format_date("2023-01-01T12:00:00.000000")
    assert result == "01.01.2023"


def test_format_date_invalid_format():
    result = format_date("invalid-date")
    assert result == "Неверный формат даты"
