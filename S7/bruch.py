class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator == 0:
            raise Exception("Division by zero is an illegal operation")
        self.denominator = denominator
        self.__reduce__()

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def setNumerator(self, newNum):
        self.numerator = newNum

    def setDenominator(self, newDen):
        self.denominator = newDen

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __print__(self):
        print(f"{self.denominator} / {self.numerator}")

    def __reduce__(self):
        while self.numerator % 2 == 0 and self.denominator % 2 == 0:
            self.numerator = self.numerator // 2
            self.denominator = self.denominator // 2

        for i in range(3, int(max(self.numerator // 2 + 1, self.denominator // 2 + 1)), 2):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator = self.numerator // i
                self.denominator = self.denominator // i

    def __mul__(self, other):
        newRational = Rational(0, 1)
        newRational.denominator = self.denominator * other.denominator
        newRational.numerator = self.numerator * other.numerator
        newRational.__reduce__()
        return newRational

    def __add__(self, other):
        newRational = Rational(0, 1)
        newRational.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        newRational.denominator = self.denominator * other.denominator
        newRational.__reduce__()
        return newRational

    def __sub__(self, other):
        newRational = Rational(0, 1)
        newRational.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        newRational.denominator = self.denominator * other.denominator
        newRational.__reduce__()
        return newRational

    def __truediv__(self, other):
        newRational = Rational(0, 1)
        newRational.denominator = self.denominator * other.numerator
        newRational.numerator = self.numerator * other.denominator
        newRational.__reduce__()
        return newRational
