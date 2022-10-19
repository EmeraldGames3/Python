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
    number = int(input("Enter a number: "))
    square = cmath.sqrt(number).real
    if square - int(square) < 0.5:
        print(int(square))
    else:
        print(int(square) + 1)


def b():
    lst = [1, 3, 5, 7, 10, 40, 41, 1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(lst)
    temp = []
    result = []

    for index in range(len(lst) - 1):
        if Utils.isPrime(abs(lst[index] - lst[index + 1])):
            temp.append(lst[index])
        else:
            if len(temp) > len(result):
                result = temp
            temp = []

    if Utils.isPrime(abs(lst[-1] - lst[-2])):
        temp.append(lst[-1])
    if len(temp) > len(result):
        result = temp

    print(result)
