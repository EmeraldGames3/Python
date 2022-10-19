def ggT(x, y):
    x = abs(x)
    y = abs(y)
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def kgV(x, y):
    return x * y // ggT(x, y)


def kgV_7(lst):
    index1 = int(input("Enter index1: ").strip())
    index2 = int(input("Enter index2: ").strip())
    k = lst[index1]
    for i in range(index1, index2):
        k = kgV(k, lst[i + 1])

    print("7: " + str(k))
