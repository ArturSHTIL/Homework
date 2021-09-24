a = "I am global variable!"


def enclosing_function():
    """
    Find a way to call inner_function without moving it from inside of enclosed_function.
    :return: I am local variable!
    """
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    return inner_function


def enclosing_function_2():
    """
    Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function.
    :return: I am variable from enclosed function!
    """

    a = "I am variable from enclosed function!"

    def inner_function():
        b = "I am local variable!"
        print(a)

    return inner_function


def enclosing_function_3():
    """
    Modify ONE LINE in inner_function to make it print variable 'a' from global scope
    :return: I am global variable!
    """

    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function


if __name__ == '__main__':
    first = enclosing_function()
    first()
    second = enclosing_function_2()
    second()
    third = enclosing_function_3()
    third()
