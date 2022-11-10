def readLetter():
    return input("Enter a letter ").strip()


def writeToFile(fileName, content):
    f = open(fileName, "a")

    f.write(content)


def clearFile(fileName):
    f = open(fileName, "w")
    f.write("")
