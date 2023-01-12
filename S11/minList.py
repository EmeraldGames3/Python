
def non_existent_min(l):
    def find(start, end):
        if start > end:
            return end + 1
        if start == l[start]:
            return start

        mid = (start + end) // 2

        if mid == l[mid]:
            return find(mid + 1, end)
        return find(start, mid)

    return find(0, len(l))


print(non_existent_min([1, 2, 3]))
