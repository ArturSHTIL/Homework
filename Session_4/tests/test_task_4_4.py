from Session_4 import task_4_4


def test_split_indexes_string_positive():
    actual_result = task_4_4.split_by_indexes("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
    assert actual_result == ["python", "is", "cool", ",", "isn't", "it?"]


def test_split_indexes_string_negative():
    actual_result = task_4_4.split_by_indexes("no luck", [42])
    assert actual_result == ["no luck"]


def test_split_indexes_string_positive_2():
    actual_result = task_4_4.split_by_indexes("no luck", [-4])
    assert actual_result == ["no ", "luck"]


def test_split_indexes_string_negative_2():
    actual_result = task_4_4.split_by_indexes("no luck", [-42])
    assert actual_result == ["no luck"]
