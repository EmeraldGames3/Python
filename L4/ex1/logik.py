from ex1.data import moveTrtInterpretation, characterDict, moveTrt, moveTrtName, additionalChr
from ex1.ui import printHumanOptions


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


def saveAdditionalChr():
    """
    Save the contents of additionalChr to the file
    """
    fl = open("ex1.txt", "w")

    for key in additionalChr:
        fl.write(":" + key + ":" + "+" + "\n")
        s = additionalChr[key]

        s = s.strip()

        s = s.split("+")
        # print(s)

        for word in s:
            if word != "":
                fl.write(word + "+" + "\n")

    fl.close()


def characterCreation(tur, fileWords):
    """
    Here a character is created
    :param tur: The turtle
    :param fileWords: A list of all characters in the file
    """
    characterName = ":" + input("Name your character ") + ":"

    if characterName in fileWords:
        print("Invalid name")
        return

    auxName = characterName.split(":")[1]
    additionalChr[auxName] = ""
    printHumanOptions()

    fileWords.append(characterName)

    while True:
        yorOption = input("Your character ").strip()
        if yorOption in moveTrt:
            moveTrt[yorOption](tur)
            fileWords.append(str(moveTrtName[yorOption]))
            additionalChr[auxName] += str(moveTrtName[yorOption] + "+")
        else:
            break


def writeCharacter(tur, optionChr):
    """
    We use this function to write a letter
    :param tur: The turtle
    :param optionChr: The charakter that needs to be writen
    """
    if optionChr in characterDict:
        tur.pd()
        characterDict[optionChr](tur)
        tur.pu()
    if optionChr in additionalChr:
        tur.pd()
        interpretListOfCharacters(additionalChr[optionChr], tur)
        tur.fd(30)
        tur.pu()


def writeCharacterList(tur, st):
    """
    :param tur: The turtle
    :param st: The word given by the human
    Splits the given word into characters to be written by the writeCharacter function
    """
    newS = []
    s = ""

    for c in st:
        # print(c)
        if s in additionalChr:
            newS.append(s)
            s = ""
        if c in characterDict:
            newS.append(c)
        else:
            s += c

    if s in additionalChr:
        newS.append(s)

    # print(newS)

    for e in newS:
        writeCharacter(tur, e)


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
