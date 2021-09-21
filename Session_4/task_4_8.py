def get_pairs(pair: list) -> list[tuple]:
    """
    Implement a function get_pairs(lst: List) -> List[Tuple]
    which returns a list of tuples containing pairs of elements.
    Pairs should be formed as in the example.
    If there is only one element in the list return None instead

    :param pair: [1, 2, 3, 8, 9]
    :return: [(1, 2), (2, 3), (3, 8), (8, 9)]
    """

    pair_list = []
    for i in range(len(pair) - 1):
        pair_list.append((pair[i], pair[i + 1]))
    return pair_list if pair_list else None


if __name__ == '__main__':
    print(get_pairs([1, 2, 3, 8, 9]))
