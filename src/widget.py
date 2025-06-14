from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа"""
    if not isinstance(type_and_number, str):
        return "Ошибка: Входные данные должны быть строкой."
    type_and_number_lower = type_and_number.lower()
    if "счет" in type_and_number_lower:
        account_number = type_and_number.split()[-1]  # Получаем номер счета, предполагая, что он - последнее слово
        masked_account = get_mask_account(account_number)
        if "Ошибка" in masked_account:  # Проверка, что get_mask_account() не вернула ошибку
            return masked_account
        return f"Счет {masked_account}"
    card_types = ["visa", "maestro", "mastercard", "platinum", "gold", "classic"]
    if any(card_type in type_and_number_lower for card_type in card_types):
        card_number = type_and_number.split()[-1]  # Получаем номер карты, предполагая, что он - последнее слово
        masked_card = get_mask_card_number(card_number)
        return f"{type_and_number.rsplit(' ', 1)[0]} {masked_card}"  # Возвращаем название карты и маску
    else:
        return "Тип карты/счета не определен."


def get_date(data_card_number: Any) -> str:
    """Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    if not isinstance(data_card_number, str):
        return "Ошибка: Входные данные должны быть строкой."
    return data_card_number[8:10] + "." + data_card_number[5:7] + "." + data_card_number[:4]
