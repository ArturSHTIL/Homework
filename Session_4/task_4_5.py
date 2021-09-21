def get_digits(num: int) -> tuple[int]:
    """
    Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits.
    :param num: 87178291199
    :return: (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
    """

    if isinstance(num, int):
        return tuple(map(lambda x: int(x), str(abs(num))))
    return tuple()


if __name__ == '__main__':
    print(get_digits(123456789))
