def inter(right, left):
    l = []
    i = j = 0

    while i < len(right) and j < len(left):
        if right[i] < left[i]:
            l.append(right[i])
            i += 1
        else:
            l.append(left[j])
            j += 1

    l += right[i:]
    l += left[j:]

    return l


print(inter([1, 2, 3, 8, 9], [4, 5, 6, 7]))
