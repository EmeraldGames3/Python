from statistics import mean


def read_file():
    with(open("text.txt") as f):
        content = f.read()

        content = content.split("\n")
        return list(map(lambda x: x.split(" "), content))


# print(read_file())


def ub1():
    content = read_file()
    content = list(filter(lambda x: int(x[-1]) >= 8, content))

    noten = list(map(lambda x: int(x[-1]), content))

    m = round(mean(noten), 2)

    return m


print(ub1())


def test_ub1():
    assert ub1() == 9.67

    try:
        assert ub1() == 5
    except AssertionError:
        print("It works")


test_ub1()
