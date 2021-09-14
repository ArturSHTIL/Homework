def count_character_frequency(string_for_dict: str) -> dict:
    """
    Write a Python program to count the number of characters (character frequency)
        in a string (ignore case of letters).

    :param string_for_dict: 'Oh, it is python'
    :return: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
    """
    if not isinstance(string_for_dict, str):
        raise TypeError
    else:
        string_for_dict = string_for_dict.lower()
        count_character_symbol = {i: string_for_dict.count(i) for i in string_for_dict}
        return count_character_symbol


if __name__ == '__main__':
    print(count_character_frequency('Oh, it is python'))

