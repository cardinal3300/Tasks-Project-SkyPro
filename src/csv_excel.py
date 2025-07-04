import csv
from typing import Any, Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из CSV-файла."""
    transactions: List[Dict[str, Any]] = []
    with open(file_path, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из файла Excel."""
    try:
        df = pd.read_excel(file_path)
        data = df.to_dict(orient="records")
        return data
    except Exception as ex:
        print(f"Ошибка при чтении Excel файла: {ex}")
        return []
