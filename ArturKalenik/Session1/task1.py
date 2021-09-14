def string_length(string: str) -> int:
    """
    Write a Python program to calculate the length of a string without using the `len` function.

    :param: string
    :return: 35
    """
    if isinstance(string, str):
        length = sum([1 for _ in string])
        return length
    else:
        raise ValueError


if __name__ == '__main__':
    print(string_length('qwertycheckthelenwithoutlenfunction'))
