from Session_4 import task_4_9


def test_part_1_1_positive():
    actual_result = task_4_9.part_1_1(*["hello", "world", "python", ])
    assert actual_result == {'o'}


def test_part_2_2_positive():
    actual_result = task_4_9.part_2_2(*["hello", "world", "python", ])
    assert actual_result == {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}


def test_part_3_3_positive():
    actual_result = task_4_9.part_3_3(*["hello", "world", "python", ])
    assert actual_result == {'h', 'l', 'o'}


def test_part_4_4_positive():
    actual_result = task_4_9.part_4_4(*["hello", "world", "python", ])
    assert actual_result == {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
