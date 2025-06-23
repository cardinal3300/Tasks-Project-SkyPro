import pytest

from tests.conftest import add


def test_add_success(capsys):
    result = add(2, 3)
    assert result == 5

def test_add_error(capsys):
    with pytest.raises(TypeError):
        add("1", 2)
    assert "my_function error: TypeError. Inputs: (1, 2), {}"
