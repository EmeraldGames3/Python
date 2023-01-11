# fib = lambda ct, a, b, br, l: print(a) or fib(ct + 1, b, (lambda: a + b)(), br, l + [a]) if ct < br else print(l)
fib = lambda ct, a, b, br, l: fib(ct + 1, b, (lambda: a + b)(), br, l + [a]) if ct < br else print(l)

fib(0, 1, 1, 10, [])


def fibbonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibbonacci(n - 2) + fibbonacci(n - 1)