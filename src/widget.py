from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(type_and_number: str) -> str:
    """Функция возвращает замаскированные данные типа и номера карт или счетов"""
    if "Счет" in type_and_number.lower():
        number_card = type_and_number[-20:]
        masked_number = get_mask_account(number_card)
        return f"Счет {masked_number}"
    else:
        name_card = type_and_number[-16:]
        masked_name_card = get_mask_card_number(name_card)
        name_bank = type_and_number[-16:]
        return f"{name_bank} {masked_name_card}"


def get_date(data_card_number: str) -> str:
    """Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    data_correct = data_card_number[8:10] + "." + data_card_number[5:7] + "." + data_card_number[:4]
    return data_correct


if __name__ == "__main__":
    print(mask_account_card("Platinum Visa 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
