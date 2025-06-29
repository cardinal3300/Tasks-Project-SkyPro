import pytest
from unittest.mock import patch

from src.external_api import convert_currency

def test_rub_currency():
   assert convert_currency("RUB", 100.0) == 100.0


def test_convert_currency():
    with patch('requests.request') as mock_get:
        mock_get.return_value.json.return_value = {"result": 7850.5708}
        result = convert_currency("USD", 100.0)
        assert result == 7850.5708


# def test_currency_convertor():
#     """Тест конвертации валюты"""
#     with patch("requests.get") as mock_get:
#         mock_get.return_value.json.return_value = {"result": 7860.9512}
#         result = convert_currency("USD", 100.0)
#         assert result == 7860.9512