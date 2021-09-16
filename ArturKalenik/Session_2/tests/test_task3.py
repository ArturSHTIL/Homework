from Session_2 import task3
import pytest


def test_set_of_unique_words():
    actual_result = task3.unique_words(['red', 'white', 'black', 'red', 'green', 'black'])
    assert actual_result == ['black', 'green', 'red', 'white']


