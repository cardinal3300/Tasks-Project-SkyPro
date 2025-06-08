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
