import math


def is_prime(n) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def get_all_primes(n: int) -> list[int]:
    if n < 2:
        return []
    else:
        l = [2]

        for i in range(3, n + 1, 2):
            if is_prime(i):
                l.append(i)

        return l


print(get_all_primes(69))
