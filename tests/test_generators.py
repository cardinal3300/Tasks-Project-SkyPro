from typing import Any, Dict, Iterator, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    format_card_number,
    transaction_descriptions,
)


@pytest.mark.parametrize(
    "currency_code, expected_count, expected_ids",
    [
        ("USD", 2, [1, 2]),  # Проверка для USD
        ("EUR", 1, [3]),  # Проверка для EUR
        ("RUB", 0, []),  # Проверка для отсутствующей валюты
    ],
)
def test_filter_by_currency_parameterized(
    transactions_data: List[Dict[str, Any]], currency_code: str, expected_count: int, expected_ids: List[int]
):
    """Тестирует  filter_by_currency с использованием параметризации."""
    filtered_transactions = list(filter_by_currency(transactions_data, currency_code))
    assert len(filtered_transactions) == expected_count
    actual_ids = [tx["id"] for tx in filtered_transactions]
    assert actual_ids == expected_ids


## 1. Тестирование функции filter_by_currency


def test_filter_by_currency_valid():
    """Проверяет фильтрацию транзакций по валюте."""
    transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
    ]
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 1
    assert usd_transactions[1]["id"] == 3


def test_filter_by_currency_empty():
    """Проверяет работу функции с пустым списком транзакций."""
    transactions = []
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert usd_transactions == []


def test_filter_by_currency_no_matching_currency():
    """Проверяет, что функция обрабатывает случаи без соответствующих валютных операций."""
    transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "EUR"}}},
    ]
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert usd_transactions == []


### 2. Тестирование функции transaction_descriptions


def test_transaction_descriptions_valid():
    """Проверяет, что функция возвращает корректные описания транзакций."""
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty():
    """Проверяет работу функции с пустым списком транзакций."""
    transactions = []
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == []


def test_transaction_descriptions_with_missing_descriptions():
    """Проверяет обработку транзакций без описаний."""
    transactions = [
        {"description": "Транзакция 1"},
        {"id": 2},  # Без описания
        {"description": "Транзакция 3"},
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Транзакция 1",
        "Транзакция 3",
    ]


def test_card_number_generator_valid():
    """Проверяет генерацию номера карт в заданном диапазоне."""
    generated_numbers = list(card_number_generator(1, 3))
    assert len(generated_numbers) == 3
    assert generated_numbers[0] == "0000 0000 0000 0001"
    assert generated_numbers[1] == "0000 0000 0000 0002"
    assert generated_numbers[2] == "0000 0000 0000 0003"


### 3. Тестирование генератора card_number_generator


def test_card_number_generator_formatting():
    """Проверяет правильное форматирование номеров карт."""
    number = 1234567890123456
    formatted_number = format_card_number(number)
    assert formatted_number == "1234 5678 9012 3456"


def test_card_number_generator_edge_cases():
    """Проверяет крайние значения диапазона и завершение генерации."""
    generated_numbers = list(card_number_generator(9999999999999999, 10000000000000000))
    assert len(generated_numbers) == 0  # Надежная проверка завершения генерации
    generated_numbers = list(card_number_generator(1, 1))
    assert len(generated_numbers) == 1
    assert generated_numbers[0] == "0000 0000 0000 0001"
