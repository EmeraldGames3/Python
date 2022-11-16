def f():
    pass


def g():
    f()


g()

l = [1, 2, 3]
print(l[-0])

# WTF python
print(0 == -0)

class T:
    x = 0


v = T()
print(v.x)


def fr(self):
    return 1 == 2


print(fr(v))


print([0][0])