import logging

# Создание логгера для модуля masks
logger = logging.getLogger("masks_logger")
logger.setLevel(logging.DEBUG)

# Настройка file_handler
file_handler = logging.FileHandler("masks.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка форматтера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def obfuscate_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя видимыми только первые 6 и последние 4 цифры.
    Например: "1234 56** **** 7890"

    :param card_number: Номер карты.
    :return: Замаскированный номер карты.
    """
    if not card_number.isdigit():
        logger.error(f"Неверный формат номера карты: {card_number}")
        raise ValueError("Номер карты должен содержать только цифры.")

    if len(card_number) < 16:
        logger.error(f"Слишком короткий номер карты: {card_number}")
        raise ValueError("Номер карты должен содержать минимум 16 цифр.")

    # Форматируем маску с пробелами
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def obfuscate_account_number(account_num: str) -> str:
    if not account_num.isdigit():
        return "Некорректный номер счета"
    if len(account_num) <= 4:
        return f"**{account_num[-2:]}"
    return f"**{account_num[-4:]}"