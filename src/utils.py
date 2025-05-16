import re
from collections import Counter


def search_transactions(transactions, search_string):
    """
    Фильтрует транзакции по подстроке в описании (через re).
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [
        transaction for transaction in transactions
        if pattern.search(transaction.get("description", ""))
    ]


def categorize_transactions(transactions, key="description"):
    """
    Группирует транзакции по ключу и считает количество.
    """
    categories = [transaction.get(key, "Неизвестно") for transaction in transactions]
    return dict(Counter(categories))