from Session_2 import task5
import pytest


def test_sorted_dictionary_positive():
    actual_result = task5.sorted_dictionary({2: 3, 1: 89, 4: 5, 3: '0', 7: 3, 5: 76, 9: '17', 6: 45, 8: [2, 3]})
    assert actual_result == {1: 89, 2: 3, 3: '0', 4: 5, 5: 76, 6: 45, 7: 3, 8: [2, 3], 9: '17'}


def test_sorted_dictionary_negative():
    with pytest.raises(TypeError):
        task5.sorted_dictionary(type('Yellow'))
