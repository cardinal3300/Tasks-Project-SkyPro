from typing import Union

import pytest

from src.decorators import log


def test_log_error_console(capsys: Union) -> None:
    @log()
    def my_func(x: int, y: Union) -> None:
        return x + y

    with pytest.raises(TypeError):
        my_func(2, "3")
    captured = capsys.readouterr()
    assert "my_func: - <class 'TypeError'> - args: (2, '3') - kwargs: {}\n\n" == captured.out


def test_log_accept_console(capsys: Union) -> None:
    @log()
    def my_func() -> int:
        return 2 + 3

    assert "my_func - ok - 5" == "my_func - ok - 5"


def test_log_accept_file(capsys: Union) -> None:

    file_name = "tests/test.txt"

    @log(filename=file_name)
    def my_func(x: int, y: int) -> int:
        return x + y

    result = my_func(2, 3)
    assert result == 5

    with open(file_name, "r", encoding="UTF-8") as file:
        content = file.readlines()
        assert content[-1] == "my_func - ok - 5\n"
