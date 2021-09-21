from Session_4 import task_4_11


def test_combine_dicts_positive():
    actual_result = task_4_11.combine_dicts({'a': 200, 'b': 200}, {'a': 200, 'c': 300}, {'a': 300, 'd': 2020})
    assert actual_result == {'a': 700, 'b': 200, 'c': 300, 'd': 2020}


def test_combine_dicts_negative():
    actual_result = task_4_11.combine_dicts({'a': 200, 'b': 200}, {'a': 200, 'c': 300}, {})
    assert actual_result == {'a': 400, 'b': 200, 'c': 300}


def test_combine_dicts_negative_2():
    actual_result = task_4_11.combine_dicts({'a': 200, 'b': 200}, {'a': 200, 'c': 300}, None)
    assert actual_result == {'a': 400, 'b': 200, 'c': 300}
