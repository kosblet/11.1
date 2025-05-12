from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры."""
    card_str = str(card_number).strip()

    if len(card_str) < 6:
        return card_str  # Если слишком короткий — возвращаем как есть

    part_1 = card_str[:4]
    part_2 = card_str[4:6]
    part_3 = card_str[-4:]

    return f"{part_1} {part_2}** **** {part_3}"


def get_mask_account(card_account: Union[int, str]) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры."""
    card_account = str(card_account).strip()
    return "**" + card_account[-4:]
