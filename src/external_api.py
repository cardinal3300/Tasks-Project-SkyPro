import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"


def convert_currency(currency: str, amount: float) -> float:
    """Конвертирует валюту в рубли, предполагая наличие API-ключа и валидных данных."""
    new_currency = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={new_currency}&from={currency}&amount={amount}"

    payload: dict[str, str] = {}
    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.request("GET", url, headers=headers, data=payload)

    return float(response.json().get("result"))


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
