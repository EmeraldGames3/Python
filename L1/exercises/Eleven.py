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
    print("a")


def b():
    lst = [8, 9, 1, 14, 15, 16, 20, 19, 18, 17]
    temp = []
    result = []

    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            temp.append(lst[i - 1])
            # print(lst[i - 1])
        else:
            temp.append(lst[i - 1])
            if len(temp) > len(result):
                result = temp
            temp = []

    if lst[-2] > lst[-1]:
        temp.append(lst[-1])
    if len(temp) > len(result):
        result = temp

    print(result)
