from unittest.mock import mock_open, patch


from src.utils import reading_json_file


# Тест при верной и неверной (неполной) структуре JSON-файла
def test_reading_json_file_correct() -> None:
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"}]')):
        assert reading_json_file("") == [{"1": "2"}]
    with patch("builtins.open", mock_open(read_data='[{"1" : "2"]')):
        assert reading_json_file("") == []


def test_file_not_found() -> None:
    result = reading_json_file("nonexistent_file.json")
    assert result == []
