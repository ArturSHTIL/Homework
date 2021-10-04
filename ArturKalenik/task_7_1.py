class OpenFile(object):
    """
    Implement class-based context manager for opening and working with file,
    including handling exceptions. Do not use 'with open()'.
    Pass filename and mode via constructor.
    """

    def __init__(self, file, flag):
        self.file = file
        self.flag = flag

    def __enter__(self):
        try:
            self.fp = open(self.file, self.flag)
        except IOError:
            self.fp = open(self.file, "w")
        return self.fp

    def __exit__(self, exp_type, exp_value, exp_tr):
        if exp_type is IOError:
            self.fp.close()
            return True
        self.fp.close()


with OpenFile("example1.txt", "w") as fp:
    fp.write("Hello, World\n")
    fp.write("Tom and Jerry it's a Legend!\n")
    fp.write("Bugs Bunny is a really Cool Rabbit!\n")
    fp.write("And what do you think of Chip 'n' Dale now?\n")
