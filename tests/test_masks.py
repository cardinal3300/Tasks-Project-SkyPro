import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid(test_data):
    """Проверяет корректное маскирование номера карты."""
    assert get_mask_card_number(test_data["card_number"]) == "1234 56** **** 3456"


def test_get_mask_card_number_invalid():
    """Проверяет обработку некорректных данных."""
    assert get_mask_card_number("abc") == "Ошибка: Номер карты содержит недопустимые символы."


def test_get_mask_account_valid(test_data):
    """Проверяет корректное маскирование номера счета."""
    assert get_mask_account(test_data["check_number"]) == "**7890"


def test_get_mask_account_invalid():
    """Проверяет обработку некорректных данных для get_mask_account."""
    assert get_mask_account("abc") == "Ошибка: Номер счета содержит недопустимые символы."
