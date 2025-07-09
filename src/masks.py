import logging
import re
from typing import Any

# Объект логера:

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Any) -> str:
    """Возвращает замаскированный номер банковской карты, в формате XXXX XX** **** XXXX, где X - цифры."""
    logger.info("Запуск функции `get_mask_card_number`")
    if not isinstance(card_number, (str, int)):
        logger.error("Неверный тип данных. Ожидается строка или целое число")
        return "Ошибка: Неверный тип данных. Ожидается строка или целое число."
    card_number_str = str(card_number).replace(" ", "")
    if not re.match(r"^\d+$", card_number_str):
        logger.error("Номер карты содержит недопустимые символы")
        return "Ошибка: Номер карты содержит недопустимые символы."
    if len(card_number_str) <= 12:
        logger.error("Некорректная длина номера карты")
        return "Ошибка: Некорректная длина номера карты."
    # Блок маскировки
    masked_number = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[12:]
    logger.info("Функция отработала")
    return masked_number


def get_mask_account(check_number: Any) -> str:
    """Маскирует номер банковского счета, отображая последние 4 цифры в формате **XXXX."""
    logger.info("Запуск функции `get_mask_account`")
    check_number_str = str(check_number).replace(" ", "")
    if not re.match(r"^\d+$", check_number_str):
        logger.error("Номер счета содержит недопустимые символы")
        return "Ошибка: Номер счета содержит недопустимые символы."
    if len(check_number_str) < 4:
        logger.error("Недостаточная длина номера счета")
        return "Ошибка: Недостаточная длина номера счета."
    logger.info("Функция отработала")
    return f"**{check_number_str[-4:]}"
