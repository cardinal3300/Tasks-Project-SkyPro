import pytest


@pytest.fixture
def test_data():
    """Предоставляет общие тестовые данные для использования в тестах."""
    return {
        "card_number": "1234567890123456",
        "check_number": "1234567890",
        "date_valid": "2024-03-11T02:26:18.671407",
        "date_string": 20240311022618671407,
        "data_list": [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
    }
