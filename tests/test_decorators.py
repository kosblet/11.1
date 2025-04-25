import pytest
import sys
from src.decorators import log


@pytest.fixture
def caplog_filename(tmp_path):
    """Фикстура для создания временного файла для логов."""
    return tmp_path / "test_log.txt"


def test_log_to_console(capsys):
    """
    Проверяет логирование в консоль при успешном выполнении функции.
    """

    @log()
    def example_function(x, y):
        return x + y

    example_function(1, 2)
    captured = capsys.readouterr()
    assert "Вызов функции example_function с параметрами" in captured.out
    assert "Функция example_function успешно завершена. Результат: 3" in captured.out


def test_log_to_file(caplog_filename):
    """
    Проверяет логирование в файл при успешном выполнении функции.
    """

    @log(filename=str(caplog_filename))
    def example_function(x, y):
        return x * y

    example_function(3, 4)
    with open(caplog_filename, "r", encoding="utf-8") as f:
        log_content = f.read()
    assert "Вызов функции example_function с параметрами" in log_content
    assert "Функция example_function успешно завершена. Результат: 12" in log_content


def test_log_error_handling(capsys):
    """
    Проверяет логирование ошибок.
    """

    @log()
    def faulty_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty_function(10, 0)
    captured = capsys.readouterr()
    assert "Ошибка в функции faulty_function: ZeroDivisionError" in captured.out
    assert "Входные параметры: args=(10, 0), kwargs={}" in captured.out
