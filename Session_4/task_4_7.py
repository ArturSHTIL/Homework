def list_product_numbers(data: list[int]) -> list[int]:
    """
    Implement a function foo(List[int]) -> List[int] which, given a list of integers,
    return a new list such that each element at index i of the new list is the product
    of all the numbers in the original array except the one at i
    :param data: [1, 2, 3, 4, 5]
    :return: [120, 60, 40, 30, 24]
    """

    multi_list = []
    for i in range(len(data)):
        multiplication_result = 1
        for j in range(len(data)):
            if i != j:
                multiplication_result *= data[j]
        multi_list.append(multiplication_result)
    return multi_list


if __name__ == '__main__':
    print(list_product_numbers([1, 2, 3, 4, 5]))
