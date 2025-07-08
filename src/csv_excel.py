import pandas as pd
import csv
from typing import Any, Dict, List, Hashable

from pandas import DataFrame


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из CSV-файла."""
    transactions: List[Dict[str, Any]] = []
    with open(file_path, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions


def read_excel_transactions(file_path: str) -> List[Dict[Hashable, Any]]:
    """Считывает финансовые операции из файла Excel."""
    df = pd.read_excel(file_path)
    df = df.where(pd.notna(df), None)
    data = df.to_dict(orient="records")

    return data
