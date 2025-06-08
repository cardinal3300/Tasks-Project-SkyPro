import sys
import os

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

state_opration = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(73654108430135874305))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Счет 6468647367889477958X"))
    print(mask_account_card("Счет 600000004686473678894779589"))
    print(mask_account_card("Счет 73678894779589"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(filter_by_state(state_opration))
    print(filter_by_state(state_opration, state="CANCELED"))
    print(sort_by_date(state_opration))
