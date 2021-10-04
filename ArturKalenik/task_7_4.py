import functools


def exception(function):
    """
    Implement decorator for supressing exceptions. If exception not occure write log to console.
    :param function: args or kwargs
    :return: result
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            function_result = function(*args, **kwargs)
            print(function_result)
        except Exception:
            pass

    return wrapper


@exception
def zero_divide(a, b):
    return a / b


@exception
def str_plus_int(a, b):
    return a + b


@exception
def int_plus_int(a, b):
    return a + b


if __name__ == '__main__':
    zero_divide(1, 0)
    str_plus_int('32', 18)
    int_plus_int(131, 125)
