import functools


def remember_result(func):
    """
    Implement a decorator remember_result which remembers last result of function it decorates
    and prints it before next call.

    :param func:*args
    :return: str
    """

    user_string = None

    def wrapper(*args):
        nonlocal user_string

        print(f"Last result = {user_string}")
        int_sting = 0
        for i in args:
            if isinstance(i, int):
                int_sting += i
        if int_sting:
            args = str(int_sting)
        user_string = func(*args)

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)
