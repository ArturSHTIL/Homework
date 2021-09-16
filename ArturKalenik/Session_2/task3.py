def unique_words(words: list) -> list:
    """
    Write a Python program that accepts a comma separated sequence of words as input and
    prints the unique words in sorted form.

    :param words: ['red', 'white', 'black', 'red', 'green', 'black']
    :return: ['black', 'green', 'red', 'white']
    """
    set_unique_words = sorted(set(words))
    return set_unique_words


if __name__ == '__main__':
    print(unique_words(['red', 'white', 'black', 'red', 'green', 'black']))
