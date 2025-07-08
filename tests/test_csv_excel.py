import unittest
from typing import Any, Dict, List
from unittest.mock import Mock, patch

from src.csv_excel import read_csv_transactions, read_excel_transactions


class TestFileReadingFunctions(unittest.TestCase):

    @patch("src.csv_excel.read_csv_transactions")
    def test_read_csv_to_dict(self, mock_read_csv_transactions: Mock) -> None:
        mock_read_csv_transactions.return_value = List[Dict[str, Any]]
        data_from_csv = read_csv_transactions("data/transactions.csv")
        assert str(data_from_csv)

    @patch("src.csv_excel.read_excel_transactions")
    def test_read_excel_to_dict(self, mock_read_excel_transactions: Mock) -> None:
        mock_data: List[Dict[str, Any]] = [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": 3598919.0,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": 29740.0,
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
            {
                "id": 593027.0,
                "state": "CANCELED",
                "date": "2023-07-22T05:02:01Z",
                "amount": 30368.0,
                "currency_name": "Shilling",
                "currency_code": "TZS",
                "from": "Visa 1959232722494097",
                "to": "Visa 6804119550473710",
                "description": "Перевод с карты на карту",
            },
        ]
        mock_read_excel_transactions.return_value = mock_data

        data_from_excel = read_excel_transactions("data/transactions_excel.xlsx")

        assert data_from_excel == mock_data
        mock_read_excel_transactions.assert_called_once_with("data/transactions_excel.xlsx")
