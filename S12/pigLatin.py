def pig_latin(word: str):
    return word[1:] + word[0].lower() + "ay"


def read_file():
    # Read the contents of the file
    with(open("text.txt") as f):
        content = f.read()

        # Use repeated splits on the content of the file to transform the string in to a matrix of strings
        content = content.split("\n")
        return list(map(lambda line: line.strip(".").split(" "), content))


# print(read_file())

def ub3():
    content = read_file()
    print(content)

    pig_content = list(map(lambda line: " ".join(list(map(pig_latin, line))), content))
    print(pig_content)

    return ".\n".join(pig_content)


print(ub3())
