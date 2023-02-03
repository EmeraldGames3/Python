def shell(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            idx = i
            while idx >= gap and arr[idx - gap] > temp:
                arr[idx] = arr[idx - gap]
                idx -= gap

            arr[idx] = temp
        gap //= 2
    return arr

print(shell([35, 17, 28, 19, 29, 0, 8, 27, 4, 3]))