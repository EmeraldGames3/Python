import math

lst = [12, 14, 16, 18, 12, 13, 25, 25, 25, 48, 69, 42, 21, 61, 98, 87, 76, 12, 36]
print(lst)
key = lst[0]


def removeDuplicates_1():
    newLst = list(dict.fromkeys(lst))

    print("1: " + str(newLst))
    return newLst


def isSymmetric(a, b):
    return a % 10 == b // 10 % 10 and a // 10 % 10 == b % 10


def countSymmetricNumbers_2():
    ct = 0
    for e1 in lst:
        for e2 in lst:
            if isSymmetric(e1, e2):
                ct += 1

    ct //= 2

    print("2: " + str(ct))


def generateBigNumber_3():
    lst.sort(reverse=True)
    print(lst)

    n = 0

    for e in lst:
        n *= 100
        n += e

    print("3: " + str(n))


def encryptElements_4():
    for i in range(1, len(lst)):
        lst[i] *= key

    print("4: " + str(lst))


def decryptElements_4():
    for i in range(1, len(lst)):
        lst[i] //= key

    print(lst)


def add(a, b):
    return int(a) + int(b)


def subtract(a, b):
    return int(a) - int(b)


def multiply(a, b):
    return int(a) * int(b)


def divide(a, b):
    return int(a) // int(b)


def findOperator(s):
    if "+" in s:
        return "+"
    if "-" in s:
        return "-"
    if "*" in s:
        return "*"
    if "/" in s:
        return "/"
    return "0"


operators = {
    "+": add,
    "-": divide,
    "*": multiply,
    "/": divide,
}


def filterNumbers_5():
    print("5: ")
    list1 = [12, 32, 64, 89, 11]
    result = []
    print(list1)
    beziehung = input("Beziehung: ")
    beziehung = beziehung.strip()
    beziehung = beziehung.split("=")

    originalLeftSide = beziehung[0]
    originalRightSide = beziehung[1]

    leftSideValue = 0
    rightSideValue = 0
    rightSideValueComputed = False
    leftSideValueComputed = False

    op_left = findOperator(originalLeftSide)
    op_right = findOperator(originalRightSide)

    leftSide = originalLeftSide[:]
    rightSide = originalRightSide[:]

    if "x" not in leftSide and "y" not in leftSide:
        if op_left != "0":
            leftSide = leftSide.split(op_left)
            leftSideValue = operators[op_left](leftSide[0], leftSide[1])
        else:
            leftSideValue = int(leftSide)
        leftSideValueComputed = True
    if "x" not in rightSide and "y" not in rightSide:
        if op_right != "0":
            rightSide = rightSide.split(op_right)
            rightSideValue = operators[op_right](rightSide[0], rightSide[1])
        else:
            rightSideValue = int(rightSide)
        rightSideValueComputed = True

    # print(leftSideValue)
    # print(rightSideValue)

    if rightSideValue == leftSideValue and leftSideValueComputed and rightSideValueComputed:
        list1 = []
        print(list1)
        return

    for e in list1:
        x = e // 10
        y = e % 10

        leftSide = originalLeftSide[:]
        rightSide = originalRightSide[:]

        leftSide = leftSide.replace("x", str(x))
        leftSide = leftSide.replace("y", str(y))

        rightSide = rightSide.replace("x", str(x))
        rightSide = rightSide.replace("y", str(y))

        if not leftSideValueComputed:
            if op_left != "0":
                leftSide = leftSide.split(op_left)
                leftSideValue = operators[op_left](leftSide[0], leftSide[1])
            else:
                leftSideValue = int(leftSide)

        if not rightSideValueComputed:
            if op_right != "0":
                rightSide = rightSide.split(op_right)
                rightSideValue = operators[op_right](rightSide[0], rightSide[1])
            else:
                rightSideValue = int(rightSide)

        if rightSideValue != leftSideValue:
            result.append(e)

    list1 = result
    print(list1)


def isDomino(x, y):
    return x % 10 == y // 10 % 10


def findDominoSequence():
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


def ggT(x, y):
    x = abs(x)
    y = abs(y)
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def kgV(x, y):
    return x * y // ggT(x, y)


def kgV_7(index1, index2):
    k = lst[index1]
    for i in range(index1, index2):
        k = kgV(k, lst[i + 1])

    print("7: " + str(k))


# 1
lst = removeDuplicates_1()
# 2
countSymmetricNumbers_2()
# 3
generateBigNumber_3()
# 4
encryptElements_4()
decryptElements_4()
# 5
filterNumbers_5()
# 6
findDominoSequence()
# 7
kgV_7(len(lst) - 1, len(lst) - 2)
