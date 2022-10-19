def encryptElements_4(lst):
    key = lst[0]
    for i in range(1, len(lst)):
        lst[i] *= key

    print("4: " + str(lst))
    decryptElements_4(lst, key)


def decryptElements_4(lst, key):
    for i in range(1, len(lst)):
        lst[i] //= key
