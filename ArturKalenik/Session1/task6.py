def unique_values(dictionary: list) -> set:
    """
    Write a Python program to print all unique values of all dictionaries in a list.

    :param dictionary: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                                        {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    :return: {'S005', 'S002', 'S007', 'S001', 'S009'}
    """
    if not isinstance(dictionary, list):
        raise TypeError
    else:
        unique_val = set([val for i in dictionary for key, val in i.items()])
        return unique_val


if __name__ == '__main__':
    print(unique_values([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                         {"VIII": "S007"}]))
