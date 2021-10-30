import threading
import random
import time


class DiningPhilosopher(threading.Thread):
    running = True

    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self) -> None:
        while self.running:
            time.sleep(random.randint(5, 15))
            print(f'Philosopher {self.name} is hungry now!')
            self.eating()

    def eating(self):
        fork_1, fork_2 = self.left_fork, self.right_fork
        while self.running:
            fork_1.acquire(True)
            locked = fork_2.acquire(False)
            if locked:
                break
            fork_1.release()
            print(f"Philosopher {self.name} swaps forks.")
            fork_1, fork_2 = fork_2, fork_1
        else:
            return
        self.dining()
        fork_2.release()
        fork_1.release()

    def dining(self) -> None:
        print(f"Philosopher {self.name} starts eating.")
        time.sleep(random.randint(1, 5))
        print(f"Philosopher {self.name} finishes eating and now thinking.")


def dining_philosophers():
    forks = [threading.Lock() for i in range(5)]
    philosophers_names = ('1st', '2nd', '3rd', '4th', '5th')
    philosophers = [DiningPhilosopher(philosophers_names[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

    DiningPhilosopher.running = True
    for i in philosophers:
        i.start()
    time.sleep(20)
    DiningPhilosopher.running = False
    print("The meal is over.")


if __name__ == '__main__':
    dining_philosophers()
