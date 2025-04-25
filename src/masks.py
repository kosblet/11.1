import logging
import os

# Создаем папку logs, если она не существует
os.makedirs("logs", exist_ok=True)

# Создаем логер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Настройка file_handler для записи логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w")  # mode="w" для перезаписи файла при каждом запуске
file_handler.setLevel(logging.DEBUG)

# Формат записи логов
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)


def obfuscate_card_number(card_num: str) -> str:
    if not card_num.isdigit() or len(card_num) != 16:
        return "Некорректный номер карты"
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def obfuscate_account_number(account_num: str) -> str:
    if not account_num.isdigit():
        return "Некорректный номер счета"
    if len(account_num) <= 4:
        return f"**{account_num[-2:]}"
    return f"**{account_num[-4:]}"