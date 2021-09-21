def palindrome_string(data: str) -> str:
    """
    Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited.
    :param data: 'Dolli me em illod'
    :return: 'palindrome'
    """

    data = data.lower().replace(' ', '')
    if data[:] == data[::-1]:
        return 'palindrome'
    return 'not a palindrome'


if __name__ == '__main__':
    print(palindrome_string('In girum imus nocte et consumimur igni'))
