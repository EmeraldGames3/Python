def read_file():
    with(open("text.txt") as f):
        content = f.read()

        content = content.split("\n")
        content = " ".join(content).split(" ")
        return content


def separate_words():
    def read_file_old():
        with(open("text.txt") as f):
            return [line.strip() for line in f.read().split('\n')]

    return " ".join([line for line in read_file_old()]).split(" ")


def ub1(add_string: bool = True, add_number: bool = True):
    d = {}

    file_content = read_file()

    if add_string:
        d["strings"] = list(filter(lambda x: any(c.isdigit() for c in x), file_content))

    if add_number:
        d["symbols"] = list(filter(lambda x: any(c in "!@#$%^.," for c in x), file_content))

    print(d)


# print(separate_words())

ub1()

print(read_file())
