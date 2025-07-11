from unittest.mock import mock_open, patch

from src.utils import reading_json_file, process_bank_search, process_bank_counter


# Тест при верной и неверной (неполной) структуре JSON-файла
def test_reading_json_file_correct() -> None:
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"}]')):
        assert reading_json_file("") == [{"1": "2"}]
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"]')):
        assert reading_json_file("") == []


def test_file_not_found() -> None:
    result = reading_json_file("nonexistent_file.json")
    assert result == []


def test_process_bank_search():
    # Тест с пустыми данными
    assert process_bank_search([], []) == {}

    # Тест с данными без категорий
    data = [
        {"description": "Покупка", "amount": 100},
        {"description": "Снятие наличных", "amount": 50},
        {"description": "Покупка", "amount": 70}
    ]
    assert process_bank_search(data, []) == {}

    # Тест с данными и категориями
    data = [
        {"description": "Покупка", "amount": 100},
        {"description": "Снятие наличных", "amount": 50},
        {"description": "Покупка", "amount": 70}
    ]
    categories = ["Покупка", "Снятие наличных"]
    assert process_bank_search(data, categories) == {"Покупка": 2, "Снятие наличных": 1}

    # Тест с данными и категориями, где нет ни одной категории в данных
    data = [
        {"description": "Депозит", "amount": 200},
        {"description": "Перевод", "amount": 150}
    ]
    categories = ["Покупка", "Снятие наличных"]
    assert process_bank_search(data, categories) == {"Покупка": 0, "Снятие наличных": 0}