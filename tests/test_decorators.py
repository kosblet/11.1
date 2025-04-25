import io
import sys
import pytest
from src.decorators import log_to_stdout


def test_log_success(capsys):
    """
    Тестирование успешного выполнения функции с декоратором.
    """

    @log_to_stdout
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"
    assert result == 5


def test_log_error(capsys):
    """
    Тестирование ошибки в функции с декоратором.
    """

    @log_to_stdout
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    expected_output = "divide error: ZeroDivisionError. Inputs: (10, 0), {}"
    assert captured.out.strip() == expected_output
