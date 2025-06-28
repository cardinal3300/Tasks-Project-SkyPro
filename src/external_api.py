import os
from typing import Dict, Union

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"


def convert_currency(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    if not isinstance(transaction, dict):
        raise TypeError("Transaction must be a dictionary.")
    if not isinstance(transaction.get("currency"), str):
        raise TypeError("Currency must be a string.")
    if not isinstance(transaction.get("amount"), (int, float)):
        raise TypeError("Amount must be a number (int or float).")

    currency = transaction.get("currency", "").upper()
    amount = float(transaction.get("amount", 0))  # Преобразуем к float для надежности

    if currency == "RUB":
        return amount  # Нет необходимости конвертировать в рубли
    # Определение целевой валюты (RUB)
    to_currency = "RUB"

    # Отправка запроса к API конвертации валют
    try:
        headers = {"apikey": API_KEY}
        params = {"to": to_currency, "from": currency, "amount": amount}
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Обработка ответа API
        if data.get("success") and data.get("result") is not None:
            return float(data["result"])
        else:
            raise ValueError(f"API error: {data.get('error', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {e}")
    except (KeyError, TypeError) as e:
        raise ValueError(f"Error processing API response: {e}")
