from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Функция возвращает скрытый номер карты по правилам из числа"""

    card_number = card_number.replace(" ", "")
    mask_number = " ".join(card_number[i : i + 4] for i in range(0, len(card_number), 4))
    mask_number_list = list(mask_number)

    for i in range(len(mask_number_list)):
        if 7 <= i <= 13 and mask_number_list[i] != " ":
            mask_number_list[i] = "*"

    card_number_masked = "".join(mask_number_list)
    return card_number_masked


if __name__ == "__main__":
    print(get_mask_card_number("123 4567812 34534958903458 309580-348678"))


def get_mask_account(check_number: Any) -> str:
    """Функция возвращает последние 4 цыфры счёта по правилам из числа"""

    check_number = check_number.replace(" ", "")
    last_digits = str(check_number[-4:])
    return f"**{last_digits}"


if __name__ == "__main__":
    print(get_mask_account("122094576985768 2983740982370"))
