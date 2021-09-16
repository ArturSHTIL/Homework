def sorted_dictionary(dictionary: dict) -> dict:
    """
    Write a Python program to sort a dictionary by key.

    :param dictionary: {2: 3, 1: 89, 4: 5, 3: '0', 7: 3}
    :return: {1: 89, 2: 3, 3: '0', 4: 5, 7: 3}
    """
    if not isinstance(dictionary, dict):
        raise TypeError
    else:
        return dict(sorted(dictionary.items()))


if __name__ == '__main__':
    print(sorted_dictionary({2: 3, 1: 89, 4: 5, 3: '0', 7: 3, 5: 76, 9: '17', 6: 45, 8: [2, 3]}))
