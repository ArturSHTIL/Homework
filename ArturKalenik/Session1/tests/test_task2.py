from Session1 import task2
import pytest


def test_character_frequency_positive():
    actual_result = task2.count_character_frequency('Oh, it is python')
    assert actual_result == {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}


def test_character_frequency_negative():
    with pytest.raises(TypeError):
        task2.count_character_frequency(type(1))
