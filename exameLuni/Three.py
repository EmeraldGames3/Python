def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def recursive_binary_search1(lst, x, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        return recursive_binary_search1(lst, x, mid + 1, high) + mid + 1
    else:
        return recursive_binary_search1(lst, x, low, mid - 1)


# print(recursive_binary_search1([1, 2, 3, 5], 3, 0, len([1, 2, 3, 5])))


def recursive_binary_search(lst, x):
    if len(lst) == 0:
        return -1

    mid = len(lst) // 2

    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        return recursive_binary_search(lst[mid + 1:], x)
    else:
        return recursive_binary_search(lst[:mid], x)


print(recursive_binary_search([1, 2, 3, 4], 2))
