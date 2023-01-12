def sum_triplet(l: list, n: int):
    for i, a in enumerate(l):
        j = i + 1
        k = len(l) - 1

        while j < k:
            s = a + l[j] + l[k]

            if s == n:
                return a, l[j], l[k]

            if s > n:
                k -= 1
            else:
                j += 1

    # for i in range(len(l)):
    #     for j in range(len(l)):
    #         for k in range(len(l)):
    #             if l[i] + l[j] + l[k] == n:
    #                 return l[i], l[j], l[k]


print(sum_triplet([1, 2, 3, 9, 11], 6))
