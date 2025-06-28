import json
import os
from typing import Dict, Union
import requests


def reading_json_file(file_path: str) -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    transactions: list = []
    try:

        if not os.path.exists(file_path):
            print(f"WARNING: File not found: {file_path}")
            return transactions

        with open(file_path, 'r', encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print(f"WARNING: Invalid JSON format in: {file_path}")
                return transactions

        if not isinstance(data, list):
            print(f"WARNING: JSON data is not a list in: {file_path}")
            return transactions

        if not data:
            print(f"INFO: File is empty: {file_path}")
            return transactions

        transactions = data

    except IOError as e:
        print(f"ERROR: An I/O error occurred: {e}")
        return []

    return transactions
