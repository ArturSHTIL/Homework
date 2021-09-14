def multiplication_table(a: int, b: int, c: int, d: int):
    """
    # Write a program which makes a pretty print of a part of the multiplication table.

    :param a: 2
    :param b: 4
    :param c: 3
    :param d: 7
    :print:     3	4	5	6	7
            2	6	8	10	12	14
            3	9	12	15	18	21
            4	12	16	20	24	28
    """
    table_str = ""
    for i in range(c, d + 1):
        table_str += f"\t {i}"
    table_str += '\n'
    for j in range(a, b + 1):
        table_str += f"{j}"
        for k in range(c, d + 1):
            table_str += f"\t {j * k}"
        table_str += '\n'
    table_str = table_str.rstrip('\n')
    return table_str


if __name__ == '__main__':
    print(multiplication_table(2, 4, 3, 7))
