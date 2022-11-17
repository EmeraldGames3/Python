class account:
    def __init__(self, number: int, balance: int = 0):
        self.balance = balance
        self.number = number
        self.admin = None

    def setAdmin(self, admin):
        self.admin = admin

    def pay(self, amount):
        self.balance -= amount

    def getMoney(self, amount):
        self.balance += amount
