class NoBalance(Exception):
    pass


class DebitCard:
    def __init__(self, name: str):
        self.name = name
        self.money = 0

    def pay(self, amount: int):
        if amount > self.money:
            raise NoBalance

        self.money -= amount

        return self.money


d = DebitCard("Mihai")


# d.pay(1)

class CreditCard(DebitCard):
    def __init__(self, name: str):
        super().__init__(name)
        self.debt = 0

    def pay(self, amount: int):
        self.money -= amount

        if amount <= self.money:
            return self.money

        self.debt = abs(self.money)
        self.money = 0

    def __mul__(self, other: int):
        return [self for _ in range(other)]


c = CreditCard("Ion")

print(c * 2)
assert (c*2)[0] == (c*2)[1]