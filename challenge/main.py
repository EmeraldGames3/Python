fib = lambda ct, a, b, br, l: print(a) or fib(ct + 1, b, (lambda: a + b)(), br, l + [a]) if ct < br else print(l)

fib(0, 1, 1, 10, [])


def xn(b):
    print(b)
    xn((b - 1) ** 2 + 1)


# Tema analiza
xm = lambda b, ct, br, l: xm((b - 1) ** 2 + 1, ct + 1, br, l + [b]) if ct < br else print(l)

xm(2 - 0.001, 1, 40, [])
