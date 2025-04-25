import pytest
from src.utils import read_json_file


def test_read_json_file_valid(tmp_path):
    """Проверяет чтение корректного JSON-файла."""
    file = tmp_path / "test.json"
    file.write_text('[{"id": 1, "name": "Test"}]')
    result = read_json_file(str(file))
    assert result == [{"id": 1, "name": "Test"}]


def test_read_json_file_empty(tmp_path):
    """Проверяет чтение пустого JSON-файла."""
    file = tmp_path / "empty.json"
    file.write_text("")
    result = read_json_file(str(file))
    assert result == []


def test_read_json_file_invalid(tmp_path):
    """Проверяет чтение некорректного JSON-файла."""
    file = tmp_path / "invalid.json"
    file.write_text('{"key": "value"}')  # Не список
    result = read_json_file(str(file))
    assert result == []


def test_read_json_file_not_found():
    """Проверяет обработку отсутствующего файла."""
    result = read_json_file("nonexistent.json")
    assert result == []
