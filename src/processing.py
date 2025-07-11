

def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей, возвращая только те, у которых значение ключа 'state' соответствует заданному."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по значению ключа 'date' (в формате YYYY-MM-DD)."""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
