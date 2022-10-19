def isDomino(x, y):
    return x % 10 == y // 10 % 10


def findDominoSequence(lst):
    temp = []
    result = []

    for i in range(1, len(lst)):
        if isDomino(lst[i - 1], lst[i]):
            temp.append(lst[i - 1])
        else:
            temp.append(lst[i - 1])
            if len(temp) > len(result):
                result = temp
            temp = []

    if isDomino(lst[-1], lst[-2]):
        temp.append(lst[-1])

    if len(temp) > len(result):
        result = temp

    print("6: " + str(result))
