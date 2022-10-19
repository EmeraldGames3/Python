
def isSymmetric(a, b):
    return a % 10 == b // 10 % 10 and a // 10 % 10 == b % 10


def countSymmetricNumbers_2(lst):
    ct = 0
    for e1 in lst:
        for e2 in lst:
            if isSymmetric(e1, e2):
                ct += 1

    ct //= 2

    print("2: " + str(ct))
