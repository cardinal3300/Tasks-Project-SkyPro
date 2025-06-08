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


def test_filter_by_state_valid(test_data):
    """Проверяет фильтрацию по состоянию."""
    filtered = filter_by_state(test_data["data_list"], "EXECUTED")
    assert filtered == [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2024-02-28T12:12:12.987654"},
    ]


def test_filter_by_state_default_state(test_data):
    """Проверяет работу с параметром state по умолчанию"""
    filtered = filter_by_state(test_data["data_list"])
    assert filtered == [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2024-02-28T12:12:12.987654"},
    ]


def test_sort_by_date_valid(test_data):
    """Проверяет сортировку по дате в порядке убывания."""
    sorted_data = sort_by_date(test_data["data_list"])
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2024-02-28T12:12:12.987654"},
        {"id": 2, "state": "PENDING", "date": "2024-01-20T10:10:10.123456"},
    ]
    assert sorted_data == expected


def test_sort_by_date_reverse(test_data):
    """Проверяет сортировку по дате в обратном порядке (возрастания)."""
    sorted_data = sort_by_date(test_data["data_list"], reverse=False)
    expected = [
        {"id": 2, "state": "PENDING", "date": "2024-01-20T10:10:10.123456"},
        {"id": 3, "state": "EXECUTED", "date": "2024-02-28T12:12:12.987654"},
        {"id": 1, "state": "EXECUTED", "date": "2024-03-15T18:35:29.512364"},
    ]
    assert sorted_data == expected
