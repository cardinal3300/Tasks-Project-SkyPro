from unittest.mock import mock_open, patch

import pytest

from src.utils import convert_to_rub, reading_json_file


# Тест при верной и неверной (неполной) структуре JSON-файла
def test_reading_json_file_correct() -> None:
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"}]')):
        assert reading_json_file("") == [{"1": "2"}]
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"]')):
        assert reading_json_file("") == []


def test_file_not_found() -> None:
    result = reading_json_file("nonexistent_file.json")
    assert result == []


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
