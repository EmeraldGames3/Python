# fib = lambda ct, a, b, br, l: print(a) or fib(ct + 1, b, (lambda: a + b)(), br, l + [a]) if ct < br else print(l)
# fib = lambda ct, a, b, br, l: fib(ct + 1, b, (lambda: a + b)(), br, l + [a]) if ct < br else print(l)
#
# fib(0, 1, 1, 10, [])


def fibbonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibbonacci(n - 2) + fibbonacci(n - 1)


def cool_fibbonacci(n):
    return n if n in [0, 1] else fibbonacci(n - 2) + fibbonacci(n - 1)


one_line_fibbonacci = lambda n: n if n in [0, 1] else one_line_fibbonacci(n - 2) + one_line_fibbonacci(n - 1)

# print(one_line_fibbonacci(3))
