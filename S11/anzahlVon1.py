def enumerate_1(l: list):
    if 1 not in l:
        return

    for i in range(l.index(1), len(l)):
        if l[i] != 1:
            return i - l.index(1)


print(enumerate_1([0, 1, 1, 4]))
