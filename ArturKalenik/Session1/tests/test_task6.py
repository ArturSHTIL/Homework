from Session1 import task6
import pytest


def test_unique_values_from_dict_positive():
    actual_res = task6.unique_values([
        {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}])
    assert actual_res == {'S005', 'S002', 'S007', 'S001', 'S009'}


def test_unique_values_from_dict_negative():
    with pytest.raises(TypeError):
        task6.unique_values(type('Blue'))
