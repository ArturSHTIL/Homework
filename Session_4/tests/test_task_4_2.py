from Session_4 import task_4_2


def test_palindrome_string_positive():
    actual_result = task_4_2.palindrome_string("In girum imus nocte et consumimur igni")
    assert actual_result == 'palindrome'


def test_palindrome_string_negative():
    actual_result = task_4_2.palindrome_string('tyrun uyter')
    assert actual_result == 'not a palindrome'


def test_palindrome_string_negative_2():
    actual_result = task_4_2.palindrome_string('Moscow')
    assert actual_result == 'not a palindrome'


def test_palindrome_string_positive_2():
    actual_result = task_4_2.palindrome_string('Ballab')
    assert actual_result == 'palindrome'
