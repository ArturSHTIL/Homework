from string import ascii_lowercase as alphabet


def part_1_1(*args: str) -> set[str]:
    """
     characters that appear in all strings
    :param args: ["hello", "world", "python", ]
    :return: {'0'}
    """

    favorite_letter = set()
    for letter in args[0].lower():
        letter_count = 1
        for word in args[1:]:
            if letter in word:
                letter_count += 1
        if letter_count == len(args):
            favorite_letter.update(letter)
    return favorite_letter


def part_2_2(*args: str) -> set[str]:
    """
    characters that appear in at least one string
    :param args: ["hello", "world", "python", ]
    :return: {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
    """

    one_instance_letter = set(''.join(args).lower())
    return one_instance_letter


def part_3_3(*args: str) -> set[str]:
    """
    characters that appear at least in two strings
    :param args: ["hello", "world", "python", ]
    :return:{'h', 'l', 'o'}
    """

    uniq_letters = part_2_2(*args)
    letters = set()
    for letter in uniq_letters:
        second_letter = 0
        for word in args:
            if letter in word:
                second_letter += 1
        if second_letter > 1:
            letters.update(letter)
    return letters


def part_4_4(*args: str) -> set[str]:
    """
    characters of alphabet, that were not used in any string
    :param args: ["hello", "world", "python", ]
    :return: {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
    """

    unused_letters = set(alphabet) - part_2_2(*args)
    return unused_letters


if __name__ == '__main__':
    test_strings = ["hello", "world", "python", ]
    print(part_1_1(*test_strings))
    print(part_2_2(*test_strings))
    print(part_3_3(*test_strings))
    print(part_4_4(*test_strings))
