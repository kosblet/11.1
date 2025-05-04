import json
from unittest.mock import mock_open, patch
import pytest
from src.utils import read_json_file


def test_read_json_file_success():
    """
    Тест успешного чтения JSON-файла.
    """
    mock_data = '[{"id": 12345, "status": "COMPLETED"}]'
    mock_file = mock_open(read_data=mock_data)

    with patch('builtins.open', mock_file), \
         patch('logging.FileHandler'):  # Отключаем логирование для теста
        result = read_json_file("../data/sample.json")

    expected_result = json.loads(mock_data)
    assert result == expected_result
    mock_file.assert_called_once_with("../data/sample.json", "r", encoding="utf-8")


def test_read_json_file_empty():
    """
    Тест чтения пустого JSON-файла.
    """
    mock_data = '[]'
    mock_file = mock_open(read_data=mock_data)

    with patch('builtins.open', mock_file), \
         patch('logging.FileHandler'):
        result = read_json_file("../data/sample.json")

    assert result == []


def test_read_json_file_invalid_json():
    """
    Тест чтения некорректного JSON-файла.
    """
    mock_data = '{"invalid": "json"'
    mock_file = mock_open(read_data=mock_data)

    with patch('builtins.open', mock_file), \
         patch('logging.FileHandler'):
        result = read_json_file("../data/sample.json")

    assert result == []


def test_read_json_file_not_found():
    """
    Тест чтения несуществующего JSON-файла.
    """
    with patch('builtins.open', side_effect=FileNotFoundError), \
         patch('logging.FileHandler'):
        result = read_json_file("../data/nonexistent.json")

    assert result == []