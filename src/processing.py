from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей, возвращая только те, у которых значение ключа 'state' соответствует заданному"""
    # Проверка типов входных данных.
    for item in data:
        if not isinstance(item["state"], str):
            raise TypeError("Значение 'state' должно быть строкой.")
    # Фильтрация с использованием list comprehension.
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по значению ключа 'date' (в формате YYYY-MM-DD)"""
    # Проверка наличия ключа 'date' и его типа.
    for item in data:
        if "date" not in item:
            raise TypeError("У всех словарей должен быть ключ 'date'.")
        if not isinstance(item["date"], str):
            raise TypeError("Значение 'date' должно быть строкой.")
    return sorted(data, key=lambda x: x["date"], reverse=reverse)