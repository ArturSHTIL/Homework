class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} fly"

    def walk(self):
        return f"{self.name} bird can walk "

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class FlyingBird(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.ration = 'Bugs'

    def eat(self):
        return f"It eats mostly {self.ration}"


class NonFlyingBird:
    def __init__(self, name, ration='shark'):
        self.ration = ration
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk "

    def eat(self):
        return f"It eats mostly {self.ration}"

    def swim(self):
        return f"{self.name} bird can swim"

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


if __name__ == '__main__':
    s = SuperBird("Gull")
    print(str(s))
    print(s.eat())
    print(s.swim())
