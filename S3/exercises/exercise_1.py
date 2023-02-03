def isSumOfTwoElements(lst, n):
    l1 = dict.fromkeys(lst)

    for e in l1:
        if abs(n - e) in l1:
            return True

    return False
