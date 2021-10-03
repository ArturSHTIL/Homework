from _collections_abc import Iterable


class MySquareIterator:
    """
    Implement your custom iterator class called MySquareIterator
    which gives squares of elements of collection it iterates through
    """

    def __init__(self, string: list):
        self.item = string
        self.length = len(string)
        self.index = 0

    def instance_check(self):
        if not isinstance(self.item[self.index], int):
            raise Exception("The Value Not Integer")

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            self.instance_check()
            double = self.item[self.index]
            self.index += 1
            return double ** 2

    def __iter__(self):
        return self


if __name__ == '__main__':
    lst = [-1, 2, 3, 4, -5, 6, 7]
    itr = MySquareIterator(lst)

    for item in itr:
        print(item, end=' ')
