def return_a_dictionary(data: int) -> dict[int]:
    """
    Implement a function that takes a number as an argument and returns a dictionary,
     where the key is a number and the value is the square of that number.
    :param data: 5
    :return:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    if isinstance(data, int):
        if data > 0:
            dictionary = {i: i ** 2 for i in range(1, data + 1)}
            return dictionary
        elif data == 0:
            dictionary = {0: 0}
            return dictionary
        else:
            dictionary = {i: i ** 2 for i in range(data, 0)}
            return dictionary
    raise TypeError


if __name__ == '__main__':
    print(return_a_dictionary(5))
