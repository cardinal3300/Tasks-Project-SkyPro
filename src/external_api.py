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
