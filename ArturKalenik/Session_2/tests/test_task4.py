from Session_2 import task4
import pytest


def test_divisors_of_number_positive():
    actual_result = task4.divisors_of_number(60)
    assert actual_result == {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}


def test_divisors_of_number_negative():
    with pytest.raises(TypeError):
        task4.divisors_of_number(type('Red'))
