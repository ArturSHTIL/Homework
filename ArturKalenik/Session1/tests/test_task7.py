from Session1 import task7
import pytest


def test_from_tuple_into_integer_positive():
    actual_result = task7.tuple_to_an_integer((1, 2, 3, 4))
    assert actual_result == 1234


def test_from_tuple_into_integer_negative():
    with pytest.raises(TypeError):
        task7.tuple_to_an_integer(type('Green'))
