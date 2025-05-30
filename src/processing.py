from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует словари по заданному значению для ключа 'state'"""
    filtered_state = []
    for item in data:
        if item.get("state") == state:
            filtered_state.append(item)
    return filtered_state


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция возвращает отсортированный список по дате"""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)


if __name__ == "__main__":
    lists_ = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(lists_))
print(filter_by_state(lists_, 'CANCELED'))
print(filter_by_state(lists_, 'NOT_EXISTS'))
print(sort_by_date(lists_))
print(sort_by_date(lists_, False))
