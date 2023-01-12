def recursive_sort(l: list):
    if len(l) < 1:
        return l

    return [0] + recursive_sort(l[1:]) if l[0] == 0 else recursive_sort(l[1:]) + [1]


print(recursive_sort([1, 1, 1, 0, 0, 0, 1]))
