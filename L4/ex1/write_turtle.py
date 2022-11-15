import turtle

from ex1.alphabet import *
from ex1.punctiation import *
from ex1.turtle_move import *

tur = turtle.Turtle()

ch = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z,
    ".": point,
    "?": point,
    "!": point
}

moveTrt = {
    "W": moveForward,
    "S": moveBackwards,
    "A": rotateLeft,
    "D": rotateRight,
    "G": moveDown,
    "F": moveUp
}

moveTrtName = {
    "W": "forward",
    "S": "backwards",
    "A": "rotateLeft",
    "D": "rotateRight",
    "G": "moveDown",
    "F": "moveUp"
}


def printOptions():
    print("Enter 1 to write a letter")
    print("Enter 2 to add a character")


def printTurtleCommands():
    moveTrt.values()


def printHumanOptions():
    print("Your options are: \n"
          "Press W to move forward 10 pixels \n"
          "Press S to move backwards 10 pixels \n"
          "Press A to rotate left \n"
          "Press D to rotate right \n"
          "Press G to put pen down \n"
          "Press F to put pen up")


def writeToTurtle():
    while True:
        printOptions()
        option = input("Enter your option ").strip()

        if option == "1":
            optionChr = input("Write a letter ").strip()
            if optionChr in ch:
                ch[optionChr](tur)
        elif option == "2":
            fileWords = []

            with(open("ex1.txt") as fl):
                for line in fl:
                    fileWords.append(line.strip())

            fl = open("ex1.txt", "w")

            characterName = input("Name your character")

            if characterName in fileWords:
                print("Invalid name")
                continue

            fileWords.append("\n")
            fileWords.append(characterName)

            printHumanOptions()

            while True:
                yOption = input("Your character ").strip()
                if yOption in moveTrt:
                    moveTrt[yOption](tur)
                    fileWords.append(str(moveTrtName[yOption]))
                else:
                    break

            if fileWords[-1] != characterName:
                for word in fileWords:
                    fl.write(word + "\n")

            fl.close()

        else:
            tur.clear()
            break
