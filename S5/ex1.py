m = [
    [4, 3, 10],
    [1, 2, 10],
    [1, 1, 8]
]


def callPerfectMatrix():
    perfectMatrix(m)


def perfectMatrix(mat):
    for j in range(len(mat[0])):
        sc = 0
        for i in range(len(mat)):
            sc += mat[i][j]
        if not isPerfect(sc):
            print(False)
            return False
    print(True)
    return True


def isPerfect(n):
    sum = 1

    for i in range(2, n):
        if n % i == 0:
            sum += i
        i += 1

    return n == sum


def test_isPerfect():
    assert isPerfect(6)
    assert isPerfect(28)
    assert isPerfect(496)
    assert isPerfect(8128)

    assert not isPerfect(7)
    assert not isPerfect(9)
    assert not isPerfect(245)
    assert not isPerfect(69)
    assert not isPerfect(420)
