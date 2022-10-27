matrix = [
    ['A', 'B', 'C', 'D'],
    ['L', 'E', 'G', 'H'],
    ['Q', 'R', 'T', 'F']
]


def findListForElement(e):
    for i in range(len(matrix)):
        if e in matrix[i]:
            return i, matrix[i].index(e)


def isNeighbour(e1, e2):
    i_e1, j_e1 = findListForElement(e1)
    i_e2, j_e2 = findListForElement(e2)

    # print(i_e1, j_e1)
    # print(i_e2, j_e2)

    if i_e1 == i_e2 and (j_e1 == j_e2 + 1 or j_e1 == j_e2 - 1 or j_e1 - 1 == j_e2 or j_e1 + 1 == j_e2):
        return True

    if j_e1 == j_e2 and (i_e1 == i_e2 + 1 or i_e1 == i_e2 - 1 or i_e1 - 1 == i_e2 or i_e1 + 1 == i_e2):
        return True

    return False


def wordExists(word):
    for i in range(1, len(word)):
        if not isNeighbour(word[i-1], word[i]):
            return False

    if not isNeighbour(word[-1], word[-2]):
        return False

    return True
