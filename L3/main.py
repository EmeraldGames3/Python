from _1 import drawRectangles
from _2 import drawHeart
from _3 import drawHomes

exercises = {
    "1": drawRectangles,
    "2": drawHeart,
    "3": drawHomes
}


def printOptions():
    print("Zeichnungen:")
    print("1 Rechtecke")
    print("2 Herz")
    print("3 Haeuser")


def run():
    printOptions()
    option = input("Zeichnung: ")

    if option in exercises:
        exercises[option]()


run()
