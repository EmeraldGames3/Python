from Rational import Rational


def addRationalToList(lst, rational):
    lst.append(rational)


def removeRationalInList(lst, rational):
    if rational in lst:
        lst.remove(rational)
    else:
        print("This number is not in the list")


def removeAllOccurrencesInList(lst, rational):
    while rational in lst:
        removeRationalInList(lst, rational)


def sumOfList(lst):
    s = Rational(0, 1)

    for e in lst:
        s = s.__add__(e)


def printLst(lst):
    for e in lst:
        print(e, end=" , ")
    print()
