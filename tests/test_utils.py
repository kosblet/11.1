import pytest
from src.utils import search_transactions, categorize_transactions

@pytest.fixture
def sample_transactions():
    return [
        {"description": "Перевод от Ивана"},
        {"description": "Оплата кафе"},
        {"description": "Перевод от Петра"},
        {"description": "Покупка продуктов"},
    ]

def test_search_transactions(sample_transactions):
    result = search_transactions(sample_transactions, "Перевод")
    assert len(result) == 2
    assert all("Перевод" in t["description"] for t in result)

def test_categorize_transactions(sample_transactions):
    result = categorize_transactions(sample_transactions)
    assert result["Перевод от Ивана"] == 1
    assert result["Перевод от Петра"] == 1
    assert result["Оплата кафе"] == 1
    assert result["Покупка продуктов"] == 1