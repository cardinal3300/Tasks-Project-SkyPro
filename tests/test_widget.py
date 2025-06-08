import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


@pytest.fixture
def test_data():
    """Предоставляет общие тестовые данные для использования в тестах."""
    return {
        "card_number": "1234567890123456",
        "check_number": "1234567890",
        "date_string": "2024-03-11T02:26:18.671407",
        "data_list": [
            {"id": 1, "state": "EXECUTED", "date": "2024-03-15T18:35:29.512364"},
            {"id": 2, "state": "PENDING", "date": "2024-01-20T10:10:10.123456"},
            {"id": 3, "state": "EXECUTED", "date": "2024-02-28T12:12:12.987654"},
        ],
    }


def test_mask_account_card_account(test_data):
    """Проверяет маскирование счета."""
    assert mask_account_card("Счет 123456789012") == "Счет **9012"


def test_mask_account_card_card(test_data):
    """Проверяет маскирование карты."""
    assert mask_account_card("Visa 1234567890123456") == "Visa 1234 56** **** 3456"


def test_mask_account_card_invalid():
    """Проверяет обработку некорректного ввода mask_account_card"""
    assert mask_account_card("invalid_input") == "Тип карты/счета не определен."


def test_get_date_valid(test_data):
    """Проверяет корректное преобразование даты."""
    assert get_date(test_data["date_string"]) == "11.03.2024"
