def isPalindrom(s):
    return s == s[::-1]


def findPalindrom(f):
    d = {}
    for line in f:
        line = line.split('\n')[0]
        words = line.split(' ')
        for word in words:
            if isPalindrom(word):
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1

    return d


def call_findPalindrom():
    with(open("ex5.txt") as f):
        print(findPalindrom(f))


def test():
    with(open("ex5.txt") as f):
        assert findPalindrom(f) == {'ana': 4, 'outuo': 1, 'asddsa': 1, 'kjhhjk': 1, 'zxccxz': 1}
    with(open("ex5_test.txt") as f):
        assert findPalindrom(f) == {"cuvvuc": 16}
