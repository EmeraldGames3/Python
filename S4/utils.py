import lst_functions
from Rational import Rational


def printOptions():
    print("a Einfügen von Zahlen")
    print("b Löschen von Zahlen")
    print("c Berechnen die Summe aller Zahlen")


def a(l):
    n = (input("Enter a number ")).strip()
    pos = int((input("Enter position: ")).strip())
    if "/" in n:
        n = n.split("/")
        n[0] = n[0].strip()
        n[1] = n[1].strip()
        lst_functions.addRationalToPosition(l, Rational(int(n[0]), int(n[1])), pos)
    else:
        lst_functions.addRationalToPosition(l, Rational(int(n), 1), pos)


def b(l):
    n = (input("Enter a number ")).strip()
    if "/" in n:
        n = n.split("/")
        n[0] = n[0].strip()
        n[1] = n[1].strip()
        lst_functions.removeRationalInList(l, Rational(int(n[0]), int(n[1])))
    else:
        lst_functions.removeRationalInList(l, Rational(int(n), 1))
