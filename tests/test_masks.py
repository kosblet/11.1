import sys
import os
from src.masks import obfuscate_card_number, obfuscate_account_number

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))


def test_obfuscate_card_number_valid():
    result = obfuscate_card_number("9876543210987654")
    assert result == "9876 54** **** 7654"


def test_obfuscate_card_number_invalid_length():
    result = obfuscate_card_number("1234")
    assert result == "Некорректный номер карты"


def test_obfuscate_card_number_invalid_format():
    result = obfuscate_card_number("abcd1234efgh5678")
    assert result == "Некорректный номер карты"


def test_obfuscate_account_number_valid():
    result = obfuscate_account_number("98765432109876541234")
    assert result == "**1234"


def test_obfuscate_account_number_short():
    result = obfuscate_account_number("98765432")
    assert result == "**5432"


def test_obfuscate_account_number_very_short():
    result = obfuscate_account_number("1234")
    assert result == "**34"
