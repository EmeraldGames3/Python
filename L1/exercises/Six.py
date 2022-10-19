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
    number = int(input())
    ct2 = 0
    ct5 = 0
    while number != 0:
        while number % 2 == 0:
            ct2 += 1
            number /= 2
        while number % 5 == 0:
            ct5 += 1
            number /= 5

        number = int(input())

    print(min(ct2, ct5))


def b():
    lst = [1, 4, 3, 19]
    print(lst)
    temp = []
    result = []

    for index in range(len(lst) - 1):
        if Utils.isPrime(lst[index] + lst[index + 1]):
            temp.append(lst[index])
        else:
            temp.append(lst[index])
            if len(temp) > len(result):
                result = temp
            temp = []

    if Utils.isPrime(lst[-2] + lst[-1]):
        temp.append(lst[-1])
    if len(temp) > len(result):
        result = temp

    print(result)
