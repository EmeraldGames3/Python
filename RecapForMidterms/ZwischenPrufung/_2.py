def read_from_file():
    with open("input.txt") as f:
        content = (",".join(f.read().split("\n"))).split(",")

        return list(map(lambda x: int(x), content))


# print(read_from_file())


def get_reversed_number(number: int):
    reverse = 0

    while number > 0:
        reverse = reverse * 10 + number % 10

        number //= 10

    return reverse


def is_palindrom(number: int):
    if number == get_reversed_number(number):
        return True

    return False


def is_palindrom_3(number: int):
    number_3 = 0
    while number > 0:
        number_3 += number % 10
        number_3 *= 10

        number //= 1000

    number_3 //= 10

    # print(number_3)

    return is_palindrom(number_3)

def transfer():
    content = read_from_file()

    with open("output.txt", "w") as f:
        for number in content:
            # print(number)
            if is_palindrom_3(number):
                f.write(str(number) + '\n')


transfer()
