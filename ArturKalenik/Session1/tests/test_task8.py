from Session1 import task8


def test_multiplication_table_positive():
    actual_result = task8.multiplication_table(2, 4, 3, 7)
    assert actual_result == """\t 3	 4	 5	 6	 7
2	 6	 8	 10	 12	 14
3	 9	 12	 15	 18	 21
4	 12	 16	 20	 24	 28"""
