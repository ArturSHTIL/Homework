from time import sleep


def endless_generator():
    start_number = 1
    while True:
        yield start_number
        sleep(0.3)
        start_number += 2


def start_process() -> None:
    gen = endless_generator()
    while True:
        print(next(gen), end=' ')


if __name__ == '__main__':
    start_process()
