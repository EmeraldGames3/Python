# fib = lambda ct, a, b, br, l: print(a) or fib(ct + 1, b, (lambda: a + b)(), br, l + [a]) if ct < br else print(l)
fib = lambda ct, a, b, br, l: fib(ct + 1, b, (lambda: a + b)(), br, l + [a]) if ct < br else print(l)

# Tema analiza
xm = lambda b, ct, br, l: xm((b - 1) ** 2 + 1, ct + 1, br, l + [b]) if ct < br else print(l)

fib(0, 1, 1, 10, [])
xm(2 - 0.001, 1, 40, [])


def reverseFile():
    with open("tx.txt") as f:
        data = f.read()
        data = data[::-1]
    f = open("tx.txt", "w")
    f.write(data)


reverseFile()