from task_7_5 import *

"""
Create console program for proving Goldbach's conjecture. 
Program accepts number for input and print result. 
For pressing 'q' program successfully close. 
Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.
"""


def is_a_prime_number(check_num: int) -> bool:
    for i in range(2, check_num):
        if check_num % i == 0:
            return False
    return True


def goldbach(number: int) -> str:
    if number == 4:
        return "2 + 2 = 4"
    for i in range(3, number + 1):
        if is_a_prime_number(i):
            for j in range(i, number + 1):
                if is_a_prime_number(j) == 1:
                    if number == (i + j):
                        return f"{i} + {j} = {number}"


if __name__ == '__main__':
    while True:
        user_input = input("Enter Number Please: ")
        if user_input == 'q':
            exit('Good bay')
        else:
            try:
                check_an_even_number(int(user_input))
                print(goldbach(int(user_input)))
            except (ValueError, Error):
                print("You have entered data that does not meet the requirements.\nEnter an even number.\n")
