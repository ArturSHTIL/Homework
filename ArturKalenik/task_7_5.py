class Error(Exception):
    """Base class for other Exceptions"""
    pass


class TypeErrorError(Error):
    """When operation was applied to an object of an inappropriate type"""
    pass


class ValueOddError(Error):
    """When an odd number is called"""
    pass


class ValueErrorError(Error):
    """When invalid literal for int() with base 10"""
    pass


class ValueTypeError(Error):
    """The operation was applied to an object of an inappropriate type"""
    pass


class ValueTooSmallError(Error):
    """When a number less than two is called"""
    pass


def check_an_even_number(number: int):
    """
    Implement function for check that number is even and is greater than 2.
    Throw different exceptions for this errors.
    Custom exceptions must be derived from custom base exception(not Base Exception class)
    """

    if not isinstance(number, int):
        raise ValueTypeError('Invalid literal for int() with base 10')
    elif number <= 2:
        raise ValueTooSmallError('Number less than two is called')
    elif number % 2 != 0:
        raise ValueOddError('Odd number is called')
    elif number is None:
        raise TypeErrorError('The operation was applied to an object of an inappropriate type')
    else:
        return print(f"It's ok the {number} is even")


if __name__ == '__main__':
    check_an_even_number(1)
    check_an_even_number(2)
    check_an_even_number(7)
    check_an_even_number('4')
    check_an_even_number([])
