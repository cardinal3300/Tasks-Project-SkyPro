from unittest.mock import patch

import pytest

from src.external_api import convert_currency, convert_to_rub


def test_rub_currency() -> None:
    assert convert_currency("RUB", 100.0) == 100.0


def test_convert_currency() -> None:
    with patch("requests.request") as mock_get:
        mock_get.return_value.json.return_value = {"result": 7850.5708}
        result = convert_currency("USD", 100.0)
        assert result == 7850.5708


@pytest.mark.parametrize(
    "oper_dict, result",
    (
        ({"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}}, 7850.5708),
        ({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}, 100.0),
        ({"operation": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}, 0.0),
        ({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "cod": "RUB"}}}, 0.0),
        ({}, 0.0),
    ),
)

def test_convert_to_rub(oper_dict: dict, result: int) -> None:
    with patch("requests.request") as mock_get:
        mock_get.return_value.json.return_value = {"result": result}
        result_needs = convert_to_rub(oper_dict)
        assert result_needs == result
