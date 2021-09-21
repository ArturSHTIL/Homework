def combine_dicts(*args):
    """
    Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers)
    and combines them into one dictionary. Dict values should be summarized in case of identical keys.

    :param args:dict_1 = {'a': 100, 'b': 200}
                dict_2 = {'a': 200, 'c': 300}
                dict_3 = {'a': 300, 'd': 100}
    :return:{'a': 600, 'b': 200, 'c': 300, 'd': 100}
    """
    result = {}
    for dict_ in args:
        if dict_ != {} and dict_ is not None:
            for key in dict_:
                try:
                    result[key] += dict_[key]
                except KeyError:

                    result[key] = dict_[key]
        continue
    return result


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2, dict_3))
