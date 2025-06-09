import pytest

from src.widget import get_date, mask_account_card, get_mask_account


@pytest.mark.parametrize("input_string, expected_output",[
    ("Счет 73654108430135874305", "Счет **4305"),
    ("invalid_input", "Тип карты/счета не определен."),
    ("Счет abcdefgh", "Ошибка: Номер счета содержит недопустимые символы."),
    (1234567890, "Ошибка: Входные данные должны быть строкой."),]
                         )
def test_mask_account_card_parametrize(input_string: str, expected_output: str):
    assert mask_account_card(input_string) == expected_output


def test_mask_account_card_account(test_data):
    """Проверяет маскирование счета."""
    assert mask_account_card("Счет 123456789012") == "Счет **9012"


def test_mask_account_card_card(test_data):
    """Проверяет маскирование карты."""
    assert mask_account_card("Visa 1234567890123456") == "Visa 1234 56** **** 3456"


def test_mask_account_card_invalid(test_data):
    """Проверяет обработку некорректного ввода mask_account_card"""
    assert mask_account_card("invalid_input") == "Тип карты/счета не определен."


def test_get_date_valid(test_data):
    """Проверяет корректное преобразование даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_str(test_data):
    """Проверяет входные данные"""
    assert get_date(12345678) == "Ошибка: Входные данные должны быть строкой."
