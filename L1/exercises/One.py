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
    number = int(input("Number: "))

    for index in range(number):
        if Utils.isPrime(index):
            print(index)

    print()


def b():
    lst = [1, 3, 4, 5, 6, 1, 23, 6, 57, 5, 43, -4, 2, 6, 7, 8, 9, 10, 11, 12]
    print(lst)
    temp = []
    result = []

    for index in range(len(lst) - 1):
        if lst[index] < lst[index + 1]:
            temp.append(lst[index])
        else:
            temp.append(lst[index])
            if len(temp) > len(result):
                result = temp
            temp = []

    if lst[-2] < lst[-1]:
        temp.append(lst[-1])
    if len(temp) > len(result):
        result = temp

    print(result)
