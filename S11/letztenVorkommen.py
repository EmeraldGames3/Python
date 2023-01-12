def last_index(l: list, e):
    if e not in l:
        return

    for i in range(len(l) - 1, -1, -1):
        if l[i] == e:
            return i + 1


print(last_index([1, 1, 2], 1))
