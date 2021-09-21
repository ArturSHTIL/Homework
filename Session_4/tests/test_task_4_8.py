from Session_4 import task_4_8


def test_get_pairs_positive():
    actual_result = task_4_8.get_pairs([1, 2, 3, 8, 9])
    assert actual_result == [(1, 2), (2, 3), (3, 8), (8, 9)]


def test_get_pairs_negative():
    actual_result = task_4_8.get_pairs([1])
    assert actual_result is None


def test_get_pairs_negative_2():
    actual_result = task_4_8.get_pairs([])
    assert actual_result is None
