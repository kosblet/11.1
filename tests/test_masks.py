import pytest
from src.masks import obfuscate_card_number, obfuscate_account_number

def test_obfuscate_card_number_valid():
    result = obfuscate_card_number("9876543210987654")
    assert result == "9876 54** **** 7654"

def test_obfuscate_card_number_invalid_length():
    with pytest.raises(ValueError, match="Номер карты должен содержать минимум 16 цифр."):
        obfuscate_card_number("1234")

def test_obfuscate_card_number_invalid_format():
    with pytest.raises(ValueError, match="Номер карты должен содержать только цифры."):
        obfuscate_card_number("abcd1234efgh5678")

def test_obfuscate_account_number_very_short():
    result = obfuscate_account_number("1234")
    assert result == "**34"