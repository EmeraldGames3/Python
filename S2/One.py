l = [x for x in range(ord('a'), ord('z') + 1)]
l += [x for x in range(ord('A'), ord('Z') + 1)]

l = list(map(chr, l))

# print(l)


def count_occurrences(s: str):
    d = {}
    for c in s:
        if c.isalpha():
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

    return d


print(count_occurrences("scjhool"))
