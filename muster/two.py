class BankAccount:
    def __init__(self, owner):
        self.amount = 0
        self.owner = owner

    def withdraw(self, n):
        if self.amount > n:
            self.amount -= n
        else:
            raise Exception
