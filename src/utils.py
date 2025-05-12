def search_transactions(transactions, search_string):
    """Фильтрует транзакции по подстроке в описании."""
    return [
        transaction
        for transaction in transactions
        if search_string.lower() in transaction.get("description", "").lower()
    ]


def categorize_transactions(transactions, key="description"):
    """Группирует транзакции по указанному ключу и считает количество."""
    from collections import defaultdict

    result = defaultdict(int)
    for transaction in transactions:
        value = transaction.get(key, "Неизвестно")
        result[value] += 1
    return dict(result)
