from Session_4 import task_4_7


def test_list_product_numbers_positive():
    actual_result = task_4_7.list_product_numbers([1, 2, 3, 4, 5])
    assert actual_result == [120, 60, 40, 30, 24]


def test_list_product_numbers_negative():
    actual_result = task_4_7.list_product_numbers([])
    assert actual_result == []


def test_list_product_numbers_positive_2():
    actual_result = task_4_7.list_product_numbers([1, 2, 3, 4, -5])
    assert actual_result == [-120, -60, -40, -30, 24]


def test_list_product_numbers_positive_3():
    actual_result = task_4_7.list_product_numbers([1, 2, 3, 4, 0])
    assert actual_result == [0, 0, 0, 0, 24]
