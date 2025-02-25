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


