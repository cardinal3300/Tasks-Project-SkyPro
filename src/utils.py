import json

from src.external_api import convert_currency


def reading_json_file(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# print(reading_json_file('../data/operations.json'))


def convert_to_rub(operation: dict) -> float:
    """Функция конвертирования в рубли."""
    try:
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return float(operation["operationAmount"]["amount"])
        else:
            operation_currency = operation["operationAmount"]["currency"]["code"]
            operation_amount = operation["operationAmount"]["amount"]
            return float(convert_currency(operation_currency, operation_amount))
    except (KeyError, ValueError):
        return 0.0
