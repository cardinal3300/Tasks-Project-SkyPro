import os
import sys
from typing import Any

from pycodestyle import continued_indentation

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, format_card_number#, listify
from src.external_api import convert_currency, convert_to_rub
from src.utils import process_bank_search, reading_json_file, process_bank_counter
from src.csv_excel import read_csv_transactions, read_excel_transactions
from tests.conftest import transactions_data

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


def main() -> list[list] | list[dict] | list[Any] | None:
    """Главная функция отвечающая за основную логику проекта."""
    transaction_data: list = []

    print("""
    Привет! Добро пожаловать в программу работы
    с банковскими транзакциями.""")
    print("""
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    user_item: str = input("Введите номер пункта меню: ")
    while user_item not in ("1", "2", "3"):
        print("Неверный ввод! Введите один из предложенных пунктов в меню.")
        user_item = input("Введите номер пункта меню от 1 до 3: ")
    if user_item == "1":
        transaction_data = reading_json_file("data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif user_item == "2":
        transaction_data = read_csv_transactions("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif user_item == "3":
        transaction_data = read_excel_transactions("data/transactions_excel.xlsx")
        print("Для обработки выбран EXCEL-файл.")

    print("""
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    user_status: str = input("Введите статус фильтрации: ").upper()
    while user_status not in ("EXECUTED", "CANCELED", "PENDING"):
        print("Неверный ввод! Введите один из предложенный статусов.")
        user_status = input("Введите корректный статус фильтрации: ").upper()
    if user_status == "EXECUTED":
        transaction_data = filter_by_state(transaction_data, state=user_status)
        print("Операции отфильтрованы по статусу 'EXECUTED'")
    elif user_status == "CANCELED":
        transaction_data = filter_by_state(transaction_data, state=user_status)
        print("Операции отфильтрованы по статусу 'CANCELED'")
    elif user_status == "PENDING":
        transaction_data = filter_by_state(transaction_data, state=user_status)
        print("Операции отфильтрованы по статусу 'PENDING'")

    print("Отсортировать операции по дате? Да/Нет")
    user_date: str = input().lower()
    if user_date == "Да":
        print("Отсортировать по возрастанию или по убыванию?")
        if user_date == "по возрастанию":
            transaction_data = sort_by_date(transaction_data, False)
        elif user_date == "по убыванию":
            transaction_data = sort_by_date(transaction_data)
    elif user_date == "Нет":
        return transaction_data

    print("Выводить только рублевые транзакции? Да/Нет")
    user_transaction: str = input().title()
    while user_transaction not in ("Да", "Нет"):
        if user_transaction == "Да":
            transaction_data = list(filter_by_currency(transaction_data, "RUB"))
        elif user_transaction == "Нет":
            transaction_data = list(filter_by_currency(transaction_data, "USD"))
        else:
            return transaction_data

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_to_word: str = input().title()
    if user_to_word == "Да":
        user_to_search = input("Введите слово для поиска: ")
        transaction_data = list(process_bank_search(transaction_data, user_to_search))


    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transaction_data)}")
    for item in transaction_data:





if __name__ == "__main__":
    main()



# state_operation = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T21:33:41.9441"},
# ]
#
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160",
#     },
#     {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод с карты на карту",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229",
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657",
#     },
# ]
# json_transactions_list = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
# ]
#
#
# if __name__ == "__main__":
#     print(get_mask_card_number("123456"))
#     print(get_mask_account({123123}))
#     print(mask_account_card("Счет 14211924144426031657"))
#     print(get_date("2024-03-11T02:26:18.671407"))
#     print(get_date(20240311022618671407))
#     print(filter_by_state(state_operation, state="CANCELED"))
#     print(sort_by_date(state_operation, reverse=False))
#
#     usd_transactions = filter_by_currency(transactions, "Rub")
#     for _ in range(2):
#         print(next(usd_transactions))
#
    # descriptions = transaction_descriptions(transactions)
    # for _ in range(3):
    #     print(next(descriptions))
#
#     for card_number in card_number_generator(11115, 11119):
#         print(card_number)
#
    # print(format_card_number(1234567891011121))
#     print(convert_currency("USD", 100.0))
#     print(process_bank_search(transactions, "Перевод организации"))
#     print(process_bank_counter(json_transactions_list, "id"))
    # print(reading_json_file("data/operations.json"))
    # print(convert_to_rub(reading_json_file("data/operations.json")[1]))
    # print(read_csv_transactions("data/transactions.csv"))
    # print(read_excel_transactions("data/transactions_excel.xlsx"))
