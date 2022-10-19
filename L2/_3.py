def generateBigNumber_3(lst):
    lst.sort(reverse=True)
    print(lst)

    n = 0

    for e in lst:
        n *= 100
        n += e

    print("3: " + str(n))
