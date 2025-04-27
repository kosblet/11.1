import sys
from functools import wraps


def log_to_stdout(filename=None):
    """
    Декоратор для логирования выполнения функции.
    Логи могут быть направлены либо в stdout (по умолчанию), либо в указанный файл.

    :param filename: Необязательный параметр. Если указан, логи записываются в файл.
    :return: Декоратор.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Определяем, куда писать логи: в файл или в stdout
            if filename:
                output = open(filename, "a")  # Открываем файл для записи
            else:
                output = sys.stdout  # Используем stdout по умолчанию

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)
                # Логируем успешное выполнение
                print(f"{func.__name__} ok", file=output)
                return result
            except Exception as e:
                # Логируем ошибку
                error_message = (
                    f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                )
                print(error_message, file=output)
                if filename:
                    output.close()  # Закрываем файл после записи
                raise  # Переброс исключения
            finally:
                if filename and not output.closed:
                    output.close()  # Убедимся, что файл закрыт

        return wrapper

    return decorator