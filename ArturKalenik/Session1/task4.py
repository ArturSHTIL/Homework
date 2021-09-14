def divisors_of_number(number: int) -> set:
    """
    Create a program that asks the user for a number and then prints out a list of all the [divisors] of that number.

    :param number: 60
    :return: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
    """
    if not isinstance(number, int):
        raise TypeError

    else:
        divisors = {i for i in range(1, number + 1) if number % i == 0}
        return divisors


if __name__ == '__main__':
    print(divisors_of_number(60))
