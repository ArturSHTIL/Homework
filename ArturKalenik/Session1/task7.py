def tuple_to_an_integer(tuple_int: tuple) -> int:
    """
    Write a Python program to convert a given tuple of positive integers into an integer.

    :param tuple_int: (1, 2, 3, 4)
    :return: 1234
    """
    int_number = int(''.join(map(str, tuple_int)))
    return int_number


if __name__ == '__main__':
    print(tuple_to_an_integer((1, 2, 3, 4)))
