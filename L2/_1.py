def removeDuplicates_1(lst):
    newLst = list(dict.fromkeys(lst))

    print("1: " + str(newLst))
    return newLst
