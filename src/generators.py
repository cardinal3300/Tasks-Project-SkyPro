from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Возвращает итератор только по тем транзакциям, где валюта соответствует заданной."""
    # Валидация входных данных.
    if not isinstance(currency, str):
        raise TypeError("currency должен быть строкой.")
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount")
        if operation_amount:
            currency_info = operation_amount.get("currency")
            if currency_info:
                if currency_info.get("code") == currency:
                    yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генерирует описания транзакций из списка словарей с транзакциями."""
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, stop + 1):
        card_number_str = str(number)
        # Дополнение нулями слева до 16 символов
        if len(card_number_str) < 16:
            card_number_str = "0" * (16 - len(card_number_str)) + card_number_str
            formatted_card_number = (
                f"{card_number_str[0:4]} {card_number_str[4:8]} {card_number_str[8:12]} {card_number_str[12:]}"
            )
            yield formatted_card_number


def format_card_number(number: int) -> str:
    """Функция приведения числа к строке"""
    card_number_str = str(number)
    if len(card_number_str) < 16:
        card_number_str = "0" * (16 - len(card_number_str)) + card_number_str
    formatted_card_number = (
        f"{card_number_str[:4]} {card_number_str[4:8]} {card_number_str[8:12]} {card_number_str[12:]}"
    )
    return formatted_card_number
