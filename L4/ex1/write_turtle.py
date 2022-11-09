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


def printOptions():
    print("Enter 1 to write a letter")
    print("Enter 2 to add a character")


def printTurtleCommands():
    moveTrt.values()


def writeToTurtle():
    while True:
        printOptions()
        option = input("Enter your option ").strip()

        if option == "1":
            optionChr = input("Write a letter ").strip()
            if optionChr in ch:
                ch[optionChr](tur)
            else:
                continue
        elif option == "2":
            printTurtleCommands()
            while True:
                yourOption = input("Your command ").strip()
                if option in moveTrt:
                    moveTrt[yourOption]()
                else:
                    break
        else:
            tur.clear()
            break
