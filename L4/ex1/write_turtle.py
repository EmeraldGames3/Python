import turtle

from ex1.data import additionalChr
from ex1.logik import fillFileWordsList, characterCreation, writeCharacter, interpretListFromFile
from ex1.ui import printOptions, printHumanOptions

tur = turtle.Turtle()


def writeToTurtle():
    while True:
        interpretListFromFile()
        # print(additionalChr)

        printOptions()
        option = input("Enter your option ").strip()

        fileWords = fillFileWordsList()

        if option == "1":
            writeCharacter(tur)

        elif option == "2":
            characterName = ":" + input("Name your character ") + ":"

            if characterName in fileWords:
                print("Invalid name")
                return

            fileWords.append(characterName)

            printHumanOptions()

            characterCreation(tur, characterName, fileWords)

        else:
            tur.clear()
            break
