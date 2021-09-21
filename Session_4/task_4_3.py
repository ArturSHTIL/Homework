def without_split(data: str) -> list:
    """
    Implement a function which works the same as str.split method (without using str.split itself, of course).
    :param data: "Tudor or   not    Tudor"
    :return: ['Tudor', 'or', 'not', 'Tudor']
    """

    new_word = []
    split_list = ''
    for i in data:
        if i == ' ' and split_list != '':
            new_word.append(split_list.strip())
            split_list = ''
        elif i != ' ':
            split_list += i
        else:
            continue
    if split_list:
        new_word.append(split_list)

    return new_word


if __name__ == '__main__':
    print(without_split('kbmrb  lekelvrs   sgkmnb egkrhmbret     srdkgm'))
