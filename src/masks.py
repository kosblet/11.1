def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры.
    """
    card_str = str(card_number).strip()
    if len(card_str) < 6:
        return card_str
    part_1 = card_str[:4]
    part_2 = card_str[4:6]
    part_3 = card_str[-4:]
    return f"{part_1} {part_2}** **** {part_3}"


def mask_account(account: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры.
    """
    account_str = str(account).strip()

    # Если строка начинается с "Счет", извлекаем только цифры
    if account_str.startswith("Счет"):
        _, number = account_str.split(maxsplit=1)
        return f"Счет **{number[-4:]}"

    # Для других случаев просто возвращаем последние 4 цифры
    return f"**{account_str[-4:]}"