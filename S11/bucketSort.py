def bucket_sort(l):
    bucket_number = 3

    buckets = [[] for _ in range(bucket_number)]

    print(buckets)

    result = []
    for bucket in buckets:
        result += bucket

    return result


print(bucket_sort([1, 5, 3]))
