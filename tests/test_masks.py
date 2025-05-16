import pytest
from src.masks import mask_card_number, mask_account

def test_mask_card_number():
    assert mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert mask_card_number("1234") == "1234"
    assert mask_card_number(1234567890123456) == "1234 56** **** 3456"

def test_mask_account():
    assert mask_account("Счет 12345678901234567890") == "Счет **7890"
    assert mask_account("12345678901234567890") == "**7890"
    assert mask_account("Счет 1234") == "Счет **1234"