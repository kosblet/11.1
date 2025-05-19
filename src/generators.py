def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по заданной валюте.

    """
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions):
    """
    Генерирует описания операций из списка транзакций.

    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start, stop):
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    """
    for number in range(start, stop + 1):
        formatted_number = f"{number:016d}"  # Добавляем ведущие нули до 16 символов
        formatted_number = " ".join(
            [formatted_number[i : i + 4] for i in range(0, 16, 4)]
        )  # Разделяем на блоки по 4 цифры
        yield formatted_number
