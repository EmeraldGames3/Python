import lst_functions
from Rational import Rational

lst = [Rational(1, 2), Rational(1, 3), Rational(1, 4), Rational(1, 5)]


def printOptions():
    print("a Einfügen von Zahlen")
    print("b Löschen von Zahlen")
    print("c Berechnen die Summe aller Zahlen")
    print("d Print the list")


def _a(l):
    n = (input("Enter a number ")).strip()
    if "/" in n:
        n = n.split("/")
        n[0] = n[0].strip()
        n[1] = n[1].strip()
        lst_functions.addRationalToList(l, Rational(int(n[0]), int(n[1])))
    else:
        lst_functions.addRationalToList(l, Rational(int(n), 1))


def _b(l):
    n = (input("Enter the number you wish to remove "))


options = {
    "a": _a,
    "b": _b,
    "c": lst_functions.sumOfList,
    "d": lst_functions.printLst
}


def run():
    while True:
        printOptions()
        option = input("Your option ").strip()

        if option in options:
            options[option](lst)
        else:
            print("Invalid option")
            break


run()
