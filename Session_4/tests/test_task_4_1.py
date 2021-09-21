from Session_4 import task_4_1
import pytest


def test_replaces_string_positive():
    actual_result = task_4_1.replaces_string("\"\"sdv\'f\"SFR\'befb\'Beb\"bbe\"ber\"er\"Eb\"Berb\"sda\"we\'vv\'rv\"\"")
    assert actual_result == "\'\'sdv\"f\'SFR\"befb\"Beb\'bbe\'ber\'er\'Eb\'Berb\'sda\'we\"vv\"rv\'\'"


def test_sorted_dictionary_negative():
    with pytest.raises(TypeError):
        task_4_1.replaces_string(type(1))
