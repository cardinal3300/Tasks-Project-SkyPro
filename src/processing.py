from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей, возвращая только те, у которых значение ключа 'state' соответствует заданному"""

    # Проверка типов входных данных.
    if not isinstance(data, list):
        raise TypeError("Входные данные должны быть списком.")
    if not all(isinstance(item, dict) for item in data):
        raise TypeError("Все элементы списка должны быть словарями.")
    if not isinstance(state, str):
        raise TypeError("Параметр 'state' должен быть строкой.")
    # Фильтрация с использованием list comprehension.
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по значению ключа 'date' (в формате YYYY-MM-DD)"""
    # Валидация типов.
    if not isinstance(data, list):
        raise TypeError("Входные данные должны быть списком.")
    if not all(isinstance(item, dict) for item in data):
        raise TypeError("Все элементы списка должны быть словарями.")

    # Проверка наличия ключа 'date' и его типа.
    for item in data:
        if "date" not in item:
            raise TypeError("У всех словарей должен быть ключ 'date'.")
        if not isinstance(item["date"], str):
            raise TypeError("Значение 'date' должно быть строкой.")
    try:
        return sorted(data, key=lambda x: x["date"], reverse=reverse)
    except ValueError:
        raise ValueError("Неверный формат даты в данных.")


if __name__ == "__main__":
    lists_ = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(lists_))
    print(filter_by_state(lists_, "CANCELED"))
    print(filter_by_state(lists_, "NOT_EXISTS"))
    print(sort_by_date(lists_))
    print(sort_by_date(lists_, False))
