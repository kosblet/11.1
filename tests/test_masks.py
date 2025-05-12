import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        (1234567890123456, "1234 56** **** 3456"),
        ("1234", "1234"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        (12345678901234567890, "**7890"),
        ("1234", "**1234"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
