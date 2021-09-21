def split_by_indexes(string_: str, indexes: list[int]):
    """
    Implement a function split_by_index(s: str, indexes: List[int]) -> List[str]
    which splits the s string by indexes specified in indexes. Wrong indexes must be ignored.
    :param string_: "What's up Doc ? It' just a Python)) @By Rabbit."
    :param indexes:[6, 8, 12, 16, 20, 21, 29, 32, 38]
    :return:["What's", 'up', 'Doc?', "It's", 'just', 'a', 'Python))', '@By', 'Rabbit', '.']
    """

    d = []
    last_ind = indexes[-1]
    older_index = 0
    if len(string_) < indexes[-1]:
        return [string_]
    elif - len(string_) > indexes[0]:
        return [string_]
    else:
        for ind in indexes:
            step = string_[older_index:ind]
            d.append(step)
            older_index = ind

    d.append(string_[last_ind:])
    return d


if __name__ == '__main__':
    print(split_by_indexes("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
