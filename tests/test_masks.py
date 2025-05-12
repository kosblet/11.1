import json
import logging
from pathlib import Path

# Настройка логгера
logger = logging.getLogger(__name__)

# Создание директории для логов
log_directory = Path(__file__).parent.parent / "logs"
log_directory.mkdir(exist_ok=True)

# Настраиваем файловый обработчик логов
log_filepath = log_directory / "utils.log"
file_handler = logging.FileHandler(log_filepath, encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_json_data(file_path: str):
    """
    Загружает данные из JSON-файла и возвращает список словарей.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными или пустой список при ошибке.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Данные успешно загружены из файла.")
                return data
            logger.warning("Файл содержит данные, не являющиеся списком.")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
