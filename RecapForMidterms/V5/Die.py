import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    def __init__(self, dice_sides=6):
        self.dice = Dice(dice_sides)

    def play(self, rounds: int):
        v = 0
        for i in range(rounds):
            r = self.dice.roll()
            v += r
            print(f"You rolled {r}")

        print(v)


m = Player()
m.play(5)
