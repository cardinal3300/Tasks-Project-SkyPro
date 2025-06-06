from typing import Any
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(type_and_number: str) -> str:
    """ Маскирует номер карты или счета в зависимости от типа """

    if not isinstance(type_and_number, str):
        return "Ошибка: Входные данные должны быть строкой."

    type_and_number_lower = type_and_number.lower()
    if "счет" in type_and_number_lower:
        try:
            account_number = type_and_number.split()[-1]  # Получаем номер счета, предполагая, что он - последнее слово
            masked_account = get_mask_account(account_number)
            if "Ошибка" in masked_account: # Проверка, что get_mask_account() не вернула ошибку
                return masked_account
            return f"Счет {masked_account}"
        except IndexError:
            return "Ошибка: Не удалось извлечь номер счета."

    # Определение типа карты
    card_types = ["visa", "maestro", "mastercard", "platinum", "gold", "classic"]
    if any(card_type in type_and_number_lower for card_type in card_types):
        try:
            card_number = type_and_number.split()[-1]  # Получаем номер карты, предполагая, что он - последнее слово
            masked_card = get_mask_card_number(card_number)
            if "Ошибка" in masked_card: # Проверка, что get_mask_card_number() не вернула ошибку
                return masked_card
            return f"{type_and_number.rsplit(' ', 1)[0]} {masked_card}"  # Возвращаем название карты и маску
        except IndexError:
            return "Ошибка: Не удалось извлечь номер карты." #  Обработка ошибки, если нет номера

    else:
        return "Тип карты/счета не определен."


def get_date(data_card_number: str) -> str:
    """ Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ' """

    return data_card_number[8:10] + "." + data_card_number[5:7] + "." + data_card_number[:4]


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
