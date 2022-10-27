import lst_functions
from Rational import Rational


def printOptions():
    print("a Einfügen von Zahlen")
    print("b Löschen von Zahlen")
    print("c Berechnen die Summe aller Zahlen")
    print("d Print the list")


def a(l):
    n = (input("Enter a number ")).strip()
    if "/" in n:
        n = n.split("/")
        n[0] = n[0].strip()
        n[1] = n[1].strip()
        lst_functions.addRationalToList(l, Rational(int(n[0]), int(n[1])))
    else:
        lst_functions.addRationalToList(l, Rational(int(n), 1))


def b(l):
    n = (input("Enter the number you wish to remove "))