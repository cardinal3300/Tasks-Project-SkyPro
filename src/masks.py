import re
from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Возвращает замаскированный номер банковской карты,
    в формате XXXX XX** **** XXXX, где X - цифры"""
    if not isinstance(card_number, (str, int)):
        return "Ошибка: Неверный тип данных. Ожидается строка или число."
    card_number_str = str(card_number).replace(" ", "")
    if not re.match(r"^\d+$", card_number_str):
        return "Ошибка: Номер карты содержит недопустимые символы."
    if len(card_number_str) <= 12:
        return "Ошибка: Некорректная длина номера карты."
    # Блок маскировки
    masked_number = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[12:]
    return masked_number


def get_mask_account(check_number: Any) -> str:
    """Маскирует номер банковского счета, отображая последние 4 цифры в формате **XXXX"""
    if not isinstance(check_number, (str, int)):
        return "Ошибка: Неверный тип данных.  Ожидается строка или число."
    check_number_str = str(check_number).replace(" ", "")
    if not re.match(r"^\d+$", check_number_str):
        return "Ошибка: Номер счета содержит недопустимые символы."
    if len(check_number_str) < 4:
        return "Ошибка: Недостаточная длина номера счета."
    return f"**{check_number_str[-4:]}"
