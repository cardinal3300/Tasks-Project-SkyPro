from typing import Any, Dict, Iterator, List

import pytest

from src.generators import (
    card_number_generator,
    transaction_descriptions,
)


@pytest.fixture
def test_data():
    """Предоставляет общие тестовые данные для использования в тестах."""
    return {
        "card_number": "1234567890123456",
        "check_number": "12345678901234567890",
        "date_valid": "2024-03-11T02:26:18.671407",
        "abc": "Ошибка: Номер карты содержит недопустимые символы.",
        "date_string": 20240311022618671407,
        "data_list": [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
    }


@pytest.fixture
def transactions_data() -> List[Dict[str, Any]]:
    """Предоставляет тестовые данные для транзакций."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 7565166738306028",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-10-27T10:30:00",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {"name": "EUR", "code": "EUR"},
            },
            "description": "Перевод в евро",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321",
        },
    ]


@pytest.fixture
def card_number_string() -> str:
    """Фикстура для предоставления номера карты."""
    return "1234567890123456"


@pytest.fixture
def card_number_generator_setup() -> Iterator[str]:
    """Настройка для card_number_generator, чтобы избежать проблем с состоянием."""
    for number in card_number_generator(1, 3):
        yield number


def test_transaction_descriptions_valid(transactions_data: List[Dict[str, Any]]):
    """Тестирует генератор описаний транзакций."""
    descriptions = list(transaction_descriptions(transactions_data))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод в евро",
    ]
    assert descriptions == expected_descriptions


def test_card_number_generator_valid(card_number_generator_setup):
    """Проверяет генерацию номеров карт в заданном диапазоне."""
    assert card_number_generator_setup == "0000 0000 0000 0001"


def test_card_number_generator_formatting(card_number_generator_setup):
    """Проверяет правильное форматирование номеров карт."""
    assert card_number_generator_setup[:4] == "0000"
