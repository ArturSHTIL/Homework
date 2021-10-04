class EvenRange:
    """
    Implement an iterator class EvenRange, which accepts start and end of the interval
    as an init arguments and gives only even numbers during iteration.
    If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
    _Note: Do not use function `range()` at all_
    """

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.out_of_range_indicator = True
        self.instance_check()

    def instance_check(self):
        if not isinstance(self.start, int) or not isinstance(self.stop, int):
            raise Exception("The Value Not Integer")

    def __iter__(self):
        self.out_of_range_indicator = False
        return self

    def __next__(self):
        if self.start % 2 != 0:
            self.start += 1
        if self.start < self.stop:
            if self.start % 2 == 0:
                even_numbers = self.start
                self.start += 2
                return even_numbers
        if self.out_of_range_indicator:
            return "Out of numbers!"

        print("Out of numbers!")
        raise StopIteration()


if __name__ == '__main__':
    example1 = EvenRange(3, 14)
    for number in example1:
        print(number, end=' ')

    example2 = EvenRange(1, 5)
    print(next(example2))
    print(next(example2))
    print(next(example2))
    print(next(example2))
