class NoMoney(Exception):
    def __init__(self):
        self.message = "You are broke"


class BankAccount:
    def __init__(self, owner):
        self.amount = 0
        self.owner = owner

    def withdraw(self, n):
        if self.amount >= n:
            self.amount -= n
        else:
            raise NoMoney


class CreditBankAccount(BankAccount):
    def __init__(self, owner, credit_score):
        super().__init__(owner)
        self.credit_score = credit_score

    def withdraw(self, n):
        try:
            super().withdraw(n)
            self.credit_score += 1
        except NoMoney:
            self.credit_score -= self.credit_score