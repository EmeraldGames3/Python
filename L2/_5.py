def add(a, b):
    return int(a) + int(b)


def subtract(a, b):
    return int(a) - int(b)


def multiply(a, b):
    return int(a) * int(b)


def divide(a, b):
    try:
        return int(a) // int(b)
    except ZeroDivisionError:
        print("Illegal operation")


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
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def filterNumbers_5(lst):
    print("5: ")
    result = []
    print(lst)
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

    if rightSideValue == leftSideValue and leftSideValueComputed and rightSideValueComputed:
        lst = []
        print(lst)
        return

    for e in lst:
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

    lst = result
    print(lst)
