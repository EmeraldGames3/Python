def read_numbers():
    number = -1
    s = 0

    while number != 0:
        number = int(input("Enter a number "))
        s += number

    return s


print(read_numbers())
