import logging
import sys  # Добавлен импорт sys
from functools import wraps
from datetime import datetime


def log(filename: str = None):
    """
    Декоратор для логирования работы функции.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Настройка логгера
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if filename:
                handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
            else:
                handler = logging.StreamHandler()  # По умолчанию выводит в stderr
                handler.stream = sys.stdout  # Перенаправляем в stdout

            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            # Логирование начала выполнения
            logger.info(
                f"Вызов функции {func.__name__} с параметрами: args={args}, kwargs={kwargs}"
            )

            try:
                # Выполнение функции
                result = func(*args, **kwargs)
                # Логирование успешного завершения
                logger.info(
                    f"Функция {func.__name__} успешно завершена. Результат: {result}"
                )
                return result
            except Exception as e:
                # Логирование ошибки
                logger.error(
                    f"Ошибка в функции {func.__name__}: {type(e).__name__}. "
                    f"Входные параметры: args={args}, kwargs={kwargs}"
                )
                raise  # Переброс исключения

        return wrapper

    return decorator
