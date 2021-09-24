def sorted_file(file_1: str, file_2: str) -> None:
    """
    Open file unsorted_names.txt in data folder. Sort the names and write them
     to a new file called sorted_names.txt. Each name should start with a new line
    :param file_1: unsorted_names.txt
    :param file_2: sorted_names.txt
    :return: Sorted names to file - sorted_names.txt
    """

    with open(file_1) as first, open(file_2, 'w') as second:
        data = list(first.readlines())
        for i in sorted(data):
            second.write(i)


if __name__ == '__main__':
    file_unsorted = 'data_files/unsorted_names.txt'
    file_sorted = 'data_files/sorted_names.txt'
    sorted_file(file_unsorted, file_sorted)
