voc = ('a', 'e', 'i', 'o', 'u')


def reverse(s):
    vocS = []

    for c in s:
        if c in voc:
            vocS.append(c)

    newS = ""
    i = -1

    for c in s:
        if c not in vocS:
            newS += c
        else:
            newS += vocS[i]
            i -= 1

    return newS
