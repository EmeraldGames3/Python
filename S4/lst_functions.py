from Rational import Rational


def addRationalToList(lst, rational):
    lst.append(rational)


def addRationalToPosition(lst, rational, position):
    lst.insert(position, rational)


def removeRationalInList(lst, rational):
    for e in lst:
        if e.numerator == rational.numerator and e.denominator == rational.denominator:
            lst.remove(e)


def sumOfList(lst):
    s = Rational(0, 1)

    for e in lst:
        s = s.__add__(e)

    s.__reduce__()

    print(s)


def printLst(lst):
    for i in range(len(lst) - 1):
        print(lst[i], end=" , ")
    print(lst[-1], end="")
    print()
