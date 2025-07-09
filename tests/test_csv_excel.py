from unittest.mock import patch

from src.csv_excel import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv_transactions) -> None:
    operations = [
        {
            "id": 4699552.0,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        }
    ]
    mock_read_csv_transactions.return_value.to_dict.return_value = operations
    data_from_csv = read_csv_transactions("abcd.csv")
    assert data_from_csv == operations


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel_transactions) -> None:
    operations = [
        {
            "id": 4699552.0,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        }
    ]
    mock_read_excel_transactions.return_value.to_dict.return_value = operations
    data_from_csv = read_excel_transactions("abcd.excel")
    assert data_from_csv == operations
