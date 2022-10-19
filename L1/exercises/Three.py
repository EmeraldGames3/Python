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
    number = int(input("Enter the amount of columns for Pascals triangle "))
    column1 = [1]
    column2 = [1, 1]

    if number < 1:
        print("Invalid option")
        return

    print(column1)
    if number == 1:
        return

    print(column2)
    if number == 2:
        return

    number -= 2

    while number > 0:
        column1 = column2
        column2 = [1]

        for index in range(len(column1) - 1):
            column2.append(column1[index] + column1[index + 1])

        column2.append(1)
        print(column2)

        number -= 1


def b():
    lst = [1, 3, 4, 5, 6, 1, 23, 6, 57, 5, 43, -4, 2, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19, 23]
    temp = []
    result = []

    for i in lst:
        if Utils.isPrime(i):
            temp.append(i)
        else:
            if len(temp) > len(result):
                result = temp
            temp = []

    if len(temp) > len(result):
        result = temp

    print(result)
