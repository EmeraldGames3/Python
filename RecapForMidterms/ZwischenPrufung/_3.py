def do_stuff(s1):
    arr = [0] * (len(s1) - 1)

    for i in range(len(s1)):
        w = s1[i]

        while w >= 2 and s1[i] % w:
            w -= 1

        arr[i] = w

    for i in range(len(s1)):
        arr[i] = arr[i] == 1

    return arr

