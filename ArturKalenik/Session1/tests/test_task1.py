from Session1 import task1
import pytest


def test_for_calculate_string_length_positive():
    actual_result = task1.string_length('rtryrtetg')
    assert actual_result == len('rtryrtetg')


def test_for_calculate_string_length_negative():
    with pytest.raises(ValueError):
        task1.string_length(12345)
