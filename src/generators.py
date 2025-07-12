from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Возвращает генератор только по тем транзакциям, где валюта соответствует заданной."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
            yield transaction
        elif transaction.get("currency_code", {}) == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator[str]:
    """Генерирует описания транзакций из списка словарей с транзакциями."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str]:
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
    """Функция приведения числа к строке."""
    card_number_str = str(number)
    formatted_card_number = (
        f"{card_number_str[:4]} {card_number_str[4:8]} {card_number_str[8:12]} {card_number_str[12:]}"
    )
    return formatted_card_number
