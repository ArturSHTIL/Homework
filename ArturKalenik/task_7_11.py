from time import sleep


def fibonacci():
    """
    Implement a generator which will geterate Fibonacci numbers endlessly.
    :return: Iterator
    """
    a, b = 1, 1
    while True:
        yield a
        sleep(0.3)
        a, b = b, a + b


def start_process():
    gen = fibonacci()
    while True:
        print(next(gen), end=' ')


if __name__ == '__main__':
    start_process()
