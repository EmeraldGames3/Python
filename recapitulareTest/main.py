# def f():
#     pass
#
#
# def g(f):
#     f()
#
#
# g(f)
#
# s = ["florin salam"]
# s.append("Mr juve")
#
# # print(s)

# print( 0 == -0)

# l = [1, 2, 3]
# print(l[-0])

# print(1 == 2)

# print(l == 1)

# print([0][0])

# i = 0
# while i < 4:
#     if int(i % 3) == 0:
#         i -= 0.5
#     i += 1

# print(i)

# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# size = len(m)
# start = 0

# for start in range(size):
#     for i in range(start, size):
#         print(m[start][i], end=" ")
#
#     for i in range(start + 1, size):
#         print(m[i][start], end=" ")
#
# print()

# list1 = [10, 20]
# print(list1[1:4])

# print([[[0]], [0]][0][0][0])

# x = 2019
# x = x + x
# x = x - x
# x = x


# print(x)

# def f():
#     return 1 == 2 == True


# print(f())

# s = "mircea"

# print(s[0])


# m6 = [
#     [3, 2, 1],
#     [6, 5, 4],
#     [9, 8, 7]
# ]

# n = 4
# m1 = []
# counter = 0

# for i in range(n):
#     linie = []
#     for j in range(counter + n, counter, -1):
#         linie.append(j)
#
#     m1.append(linie)
#     counter += n

# for linie in m1:
#     print(linie)

m = [
    [12, 6, 3, 0, 6],
    [13, 7, 4, 1, 7],
    [14, 8, 5, 2, 8],
    [15, 10, 11, 9, 13],
    [15, 10, 11, 9, 420],
]

start = 0
end = len(m)


for _ in range((len(m) + 1) // 2):
    for i in range(start, end):
        print(m[start][i], end=" ")

    for i in range(start + 1, end):
        print(m[i][end - 1], end=" ")

    for i in range(end - 2, start - 1, -1):
        print(m[end - 1][i], end=" ")

    for i in range(end - 2, start, -1):
        print(m[i][start], end=" ")

    start += 1
    end -= 1

    print()
# x = 1, 2, 3
# print(x)

# x = 5
# y = 10 if x == 1 else 0
# print(y)

# print([i+i for i in '123'])

# x = 2022
# x **= 2
# print(x)

# def bar(): return 1 + 2
#
#
# foo = bar
# print(foo())

# e(n) = (-1)^n*n*(n+1)

def e(n):
    if n == 1:
        return 1 * 2

    return ((-1) ** (n + 1)) * n * (n + 1) + e(n - 1)


# print(e(3))

e2 = lambda n: (e2(n - 1) + ((-1) ** (n + 1)) * n * (n + 1)) if n != 1 else 1 * 2


# print(e2(3))

# arr = [0] * 256


def do_stuff(s1: str, s2: str):
    arr = [0] * 256
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        arr[ord(s1[i])] += 1
        arr[ord(s2[i])] -= 1

    for i in arr:
        if i:
            return False

    return True


# print(do_stuff("123", "123"))

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

l = s.split()

# for c in s:
#     l.append(c)


# print(l)

# def encode(code):
#     index = 0
#     for ch in code:
#         if ch == "+":
#             print(l[index], end="")
#             try:
#                 # if code[code.index(ch) + 1].isdigit():
#
#
#             except IndexError:
#                 a = 0
#         elif ch == ">":
#             index += 1
#         elif ch == "<":
#             index -= 1


encode(">>+<<+>+")
