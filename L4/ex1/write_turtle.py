import turtle

from ex1.logik import fillFileWordsList, characterCreation, interpretListFromFile, writeCharacterList, saveAdditionalChr
from ex1.ui import printOptions, printHumanOptions

tur = turtle.Turtle()


def writeToTurtle():
    fileWords = fillFileWordsList()
    while True:
        interpretListFromFile()
        # print(additionalChr)

        printOptions()
        option = input("Enter your option ").strip()

        fileWords = fillFileWordsList()

        if option == "1":
            optionChr = input("Enter a word ").strip()
            writeCharacterList(tur, optionChr)

        elif option == "2":
            printHumanOptions()

            characterCreation(tur, fileWords)

        else:
            saveAdditionalChr(fileWords)
            tur.clear()
            break
