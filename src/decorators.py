import sys
from functools import wraps


def log_to_stdout(func):
    """
    Декоратор для логирования выполнения функции в stdout.
    Выводит результат выполнения функции в формате:
    - 'my_function ok' при успешном выполнении.
    - 'my_function error: <тип ошибки>. Inputs: (args), {kwargs}' при ошибке.

    :param func: Функция, которую нужно декорировать.
    :return: Обернутая функция.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Выполняем функцию
            result = func(*args, **kwargs)
            # Логируем успешное выполнение
            print(f"{func.__name__} ok")
            return result
        except Exception as e:
            # Логируем ошибку
            error_message = (
                f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
            )
            print(error_message)
            raise  # Переброс исключения

    return wrapper
