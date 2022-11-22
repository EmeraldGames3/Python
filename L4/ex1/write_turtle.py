import turtle

from ex1.logik import fillFileWordsList, characterCreation, interpretListFromFile, writeCharacterList, saveAdditionalChr
from ex1.ui import printOptions

tur = turtle.Turtle()


def writeToTurtle():
    interpretListFromFile()
    fileWords = fillFileWordsList()
    while True:
        # print(additionalChr)
        # print(fileWords)

        printOptions()
        option = input("Enter your option ").strip()

        if option == "1":
            optionChr = input("Enter a word ").strip()
            writeCharacterList(tur, optionChr)

        elif option == "2":
            tur.clear()
            characterCreation(tur, fileWords)
            saveAdditionalChr()
            tur.clear()
            break

        else:
            saveAdditionalChr()
            tur.clear()
            break
