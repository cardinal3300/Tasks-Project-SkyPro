from unittest.mock import mock_open, patch

from src.utils import process_bank_counter, process_bank_search, reading_json_file


# Тест при верной и неверной (неполной) структуре JSON-файла
def test_reading_json_file_correct() -> None:
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"}]')):
        assert reading_json_file("") == [{"1": "2"}]
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"]')):
        assert reading_json_file("") == []


def test_file_not_found() -> None:
    result = reading_json_file("nonexistent_file.json")
    assert result == []


def test_process_bank_search() -> None:
    # Тест с пустыми данными
    assert process_bank_search([{}], "") == [{}]


def test_process_bank_counter() -> None:
    # Тест с пустыми данными
    assert process_bank_counter([{}], []) == {}
