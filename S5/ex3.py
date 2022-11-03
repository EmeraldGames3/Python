m1 = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]

m2 = [
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9]
]


def call_isMatrixRow():
    print(isMatrixRow(m1))


def isRow(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False

    return True


def isMatrixRow(m):
    l = []

    for i in range(len(m)):
        if i % 2 == 0:
            for j in range(len(m[i])):
                l.append(m[i][j])
        else:
            for j in range(len(m[i]) - 1, -1, -1):
                l.append(m[i][j])

    if isRow(l):
        return True

    return False


def test():
    assert isMatrixRow(m1)
    assert not isMatrixRow(m2)
