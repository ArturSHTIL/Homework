from Session_4 import task_4_6
import pytest


def test_longest_word_positive():
    actual_result = task_4_6.longest_word('Python is simple and effective!')
    assert actual_result == 'effective!'


def test_longest_word_negative():
    with pytest.raises(TypeError):
        task_4_6.longest_word(type(1))


def test_longest_word_negative_2():
    actual_result = task_4_6.longest_word('')
    assert actual_result == ''


def test_longest_word_positive_2():
    actual_result = task_4_6.longest_word('Python is simple and effective! more effective, then php')
    assert actual_result == 'effective!'
