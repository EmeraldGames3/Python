m = [
    [4, 3, 1],
    [1, 2, 1],
    [0, 5, 1],
]


def call_2():
    print(_2(m))


def sumList(l):
    s = 0
    for e in l:
        s += e
    return s


def _2(mat):
    l = []
    for e in mat:
        if sumList(e) - e[mat.index(e)] == e[mat.index(e)]:
            l.append(True)
        else:
            l.append(False)

    return l


def test_2():
    m1 = [
        [1, 2, 3],
        [4, 6, 2],
        [9, 5, 7]
    ]

    assert _2(m1) == [False, True, False]
    assert _2(m) == [True, True, False]
