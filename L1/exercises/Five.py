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
    print(Utils.decomposeNumber(number))


def b():
    lst = [1, 3, 4, -5, 6, 1, 23, 57, 5, 25, 43, -4, 2, 7, 8, 9, 10, 11, 12, 11, -13]
    print(lst)
    temp = []
    result = []

    for index in range(len(lst) - 1):
        if Utils.isRelativePrime(lst[index], lst[index + 1]):
            temp.append(lst[index])
        else:
            temp.append(lst[index])
            if len(temp) > len(result):
                result = temp
            temp = []

    if Utils.isRelativePrime(lst[-2], lst[-1]):
        temp.append(lst[-1])
    if len(temp) > len(result):
        result = temp

    print(result)
