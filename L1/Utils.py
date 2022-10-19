import cmath


def isPrime(number):
    if number == 0 or number == 1:
        return False
    if number % 2 == 0:
        if number == 2:
            return True
        return False

    i = 3

    while i < int((cmath.sqrt(number) + 1).real):
        if number % i == 0:
            return False
        i += 2

    return True


def cmmdc(x, y):
    x = abs(x)
    y = abs(y)

    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def decomposeNumber(x):
    number = 0
    exponent = 0
    result = ""
    fist = True
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            while x % i == 0:
                number = i
                exponent += 1
                x /= i
            if fist:
                result += str(number) + "^" + str(exponent)
                fist = False
            else:
                result += "*" + str(number) + "^" + str(exponent)

    return result


def isRelativePrime(a, b):
    if cmmdc(a, b) == 1:
        return True
    return False


def hasSameDigits(a, b):
    v1 = []
    v2 = []
    for i in range(10):
        v1.append(0)
    for i in range(10):
        v2.append(0)

    while a != 0:
        v1[a % 10] += 1
        a //= 10

    while b != 0:
        v2[b % 10] += 1
        b //= 10

    for i in range(len(v1)):
        if v1[i] > 0 and v2[i] == 0:
            return False
        if v1[i] == 0 and v2[i] > 0:
            return False

    return True
