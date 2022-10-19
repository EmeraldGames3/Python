import cmath

import Utils


def run():
    option = input("Enter a or b ").strip()
    if option == "a":
        a()
    elif option == "b":
        b()
    else:
        print("Invalid option")


def a():
    number = int(input("enter a number: "))

    for aN in range(2, int(cmath.sqrt(number).real) + 1):
        bN = number - aN
        if Utils.isPrime(aN) and Utils.isPrime(bN):
            print(str(aN) + "+" + str(bN))
            break


def b():
    print("b")
