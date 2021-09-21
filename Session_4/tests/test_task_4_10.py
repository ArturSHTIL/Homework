from Session_4 import task_4_10
import pytest


def test_return_a_dictionary_positive():
    actual_result = task_4_10.return_a_dictionary(6)
    assert actual_result == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}


def test_return_a_dictionary_positive2():
    actual_result = task_4_10.return_a_dictionary(-6)
    assert actual_result == {-1: 1, -2: 4, -3: 9, -4: 16, -5: 25, -6: 36}


def test_return_a_dictionary_negative():
    actual_result = task_4_10.return_a_dictionary(0)
    assert actual_result == {0: 0}


def test_return_a_dictionary_negative2():
    with pytest.raises(TypeError):
        task_4_10.return_a_dictionary(type('8'))
