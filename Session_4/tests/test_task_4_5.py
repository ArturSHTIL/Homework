from Session_4 import task_4_5


def test_actual_result_positive():
    actual_result = task_4_5.get_digits(87178291199)
    assert actual_result == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)


def test_actual_result_positive_2():
    actual_result = task_4_5.get_digits(-87178291199)
    assert actual_result == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)


def test_actual_result_negative():
    actual_result = task_4_5.get_digits("!!!!")
    assert actual_result == ()


