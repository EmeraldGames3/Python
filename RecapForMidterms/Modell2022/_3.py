from functools import reduce


def recursive_str(s: str):
    if s[0] != "(":
        return recursive_str(s[1:])
    elif s[-1] != ")":
        return recursive_str(s[:-1])

    return s


# print(recursive_str("Ana(rst)aksafksanfkasnfkasnfknskq"))

def matrix_sum(m: list[list]):
    return reduce(lambda x, l: x + sum(l), m, 0)


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix_sum(mat))
