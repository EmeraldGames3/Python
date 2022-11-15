from ex1.data import moveTrtInterpretation, ch, moveTrt, moveTrtName, additionalChr


def fillFileWordsList():
    """
    Opens the file and returns a list with all user defined characters
    :return: The filled list
    """
    fileWords = []
    with(open("ex1.txt") as fl):
        for line in fl:
            fileWords.append(line.strip())

    return fileWords


def characterCreation(tur, characterName, fileWords):
    """
    Here a character is created and then stored in the file
    :param tur: The turtle
    :param characterName: The name of the character to be added
    :param fileWords: A list of all characters in the file
    """
    fl = open("ex1.txt", "w")

    while True:
        yorOption = input("Your character ").strip()
        if yorOption in moveTrt:
            moveTrt[yorOption](tur)
            fileWords.append(str(moveTrtName[yorOption]))
        else:
            break

    if fileWords[-1] != characterName:
        for word in fileWords:
            if "+" not in word:
                fl.write(word + "+" + "\n")
            else:
                fl.write(word + "\n")

    fl.close()


def writeCharacter(tur):
    """
    We use this function to write a letter
    :param: The turtle
    """
    optionChr = input("Write a letter ").strip()
    if optionChr in ch:
        ch[optionChr](tur)
    if optionChr in additionalChr:
        interpretListOfCharacters(additionalChr[optionChr], tur)
        tur.fd(30)


def interpretCharacter(s, tur):
    """
    :param tur: The turtle
    :param s: A command under string form
    This function interprets the command and executes it
    """
    if s in moveTrtInterpretation:
        moveTrtInterpretation[s](tur)


def interpretListOfCharacters(l, tur):
    """
    :param l: A list of commands as a single string
    :param tur: The turtle
    Used to execute all commands in the list
    """
    l = l.split("+")
    for s in l:
        interpretCharacter(s, tur)


def interpretListFromFile():
    """
    Interprets the contents of the file and saves them in the additionalChr dictionary
    """
    s = ""
    with(open("ex1.txt") as f):
        for line in f:
            line = line.strip()
            # print(line)
            s += line

    s = s.split(":")
    # print(s)

    for i in range(1, len(s) - 1, 2):
        additionalChr[s[i]] = s[i + 1]