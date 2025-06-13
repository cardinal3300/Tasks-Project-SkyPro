from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid(test_data: str) -> str:
    """Проверяет корректное маскирование номера карты."""
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_get_mask_card_number_invalid(test_data: str) -> str:
    """Проверяет обработку некорректных данных."""
    assert get_mask_card_number("abc") == "Ошибка: Номер карты содержит недопустимые символы."


def test_get_mask_card_number_length(test_data: str) -> str:
    """Проверяет корректную длину счета для get_mask_card_number"""
    assert get_mask_card_number("123456") == "Ошибка: Некорректная длина номера карты."


def test_get_mask_account_valid(test_data: str) -> str:
    """Проверяет корректное маскирование номера счета."""
    assert get_mask_account("12345678901234567890") == "**7890"


def test_get_mask_account_invalid(test_data: str) -> str:
    """Проверяет обработку некорректных данных для get_mask_account."""
    assert get_mask_account("123jlkhb123") == "Ошибка: Номер счета содержит недопустимые символы."


def test_get_mask_account_length(test_data: str) -> str:
    """Проверяет корректную длину счета для get_mask_account."""
    assert get_mask_account("123") == "Ошибка: Недостаточная длина номера счета."
