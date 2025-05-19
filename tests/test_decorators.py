import io
import os
import sys

import pytest

from src.decorators import log_to_stdout


def test_log_success_to_console(capsys):
    """
    Тестирование успешного выполнения функции с логированием в консоль.
    """

    @log_to_stdout()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"
    assert result == 5


def test_log_error_to_console(capsys):
    """
    Тестирование ошибки в функции с логированием в консоль.
    """

    @log_to_stdout()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    expected_output = "divide error: ZeroDivisionError. Inputs: (10, 0), {}"
    assert captured.out.strip() == expected_output


def test_log_success_to_file(tmp_path):
    """
    Тестирование успешного выполнения функции с логированием в файл.
    """
    log_file = tmp_path / "log.txt"

    @log_to_stdout(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)

    # Проверяем содержимое файла
    with open(log_file, "r") as f:
        log_content = f.read().strip()

    assert log_content == "multiply ok"
    assert result == 20


def test_log_error_to_file(tmp_path):
    """
    Тестирование ошибки в функции с логированием в файл.
    """
    log_file = tmp_path / "log.txt"

    @log_to_stdout(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # Проверяем содержимое файла
    with open(log_file, "r") as f:
        log_content = f.read().strip()

    expected_output = "divide error: ZeroDivisionError. Inputs: (10, 0), {}"
    assert log_content == expected_output
