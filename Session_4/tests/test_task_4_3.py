from Session_4 import task_4_3


def test_without_split_positive():
    actual_result = task_4_3.without_split("if you want   to be ok,   study Python for every day")
    assert actual_result == ['if', 'you', 'want', 'to', 'be', 'ok,', 'study', 'Python', 'for', 'every', 'day']


def test_without_split_negative():
    actual_result = task_4_3.without_split('Hollywood')
    assert actual_result == ['Hollywood']
