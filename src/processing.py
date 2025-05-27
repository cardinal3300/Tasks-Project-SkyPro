from typing import List, Dict, Any

def filter_by_state(data: List[Dict[str, Any]], state: str="EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует словари по заданному значению для ключа 'state'"""
    filtered_state = []
    for item in data:
        if item.get("state") == state:
            filtered_state.append(item)
    return filtered_state


lists_ = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

if __name__ == "__main__":
    print(filter_by_state(lists_))


# def sort_by_date(data: list[dict], reverse=True) -> list[dict]:
#
#     sorted_list = sorted(list_of_dicts, key=lambda x: datetime get_date),reverse=reverse)
#     return sorted_list