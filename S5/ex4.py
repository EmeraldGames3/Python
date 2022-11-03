def returnLongestWord(f):
    l = []
    for line in f:
        line = line.split('\n')[0]
        words = line.split(' ')
        maxW = 0
        for w in words:
            if len(w) > maxW:
                maxW = len(w)

        l.append(maxW)
    return l


def callReturnLongestWord():
    with(open("ex4.txt") as f):
        print(returnLongestWord(f))


def test():
    with(open("ex4.txt") as f):
        assert returnLongestWord(f) == [6, 7, 7, 2]

    with(open("ex4_test1.txt") as f):
        assert returnLongestWord(f) == [4, 6, 4, 9]
