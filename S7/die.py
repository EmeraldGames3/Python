import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = random.randint(1, 6)

    def roll(self):
        self.value = random.randint(1, self.sides)


d = Die(10)

while d.value != 6:
    d.roll()

print(d.value)
