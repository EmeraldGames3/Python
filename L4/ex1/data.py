from ex1.alphabet import *
from ex1.punctiation import point, exclamationMark, questionMark
from ex1.turtle_move import moveForward, moveBackwards, rotateLeft, rotateRight, moveDown, moveUp

"""
This is a dictionary that contains all functions for characters 
"""
characterDict = {
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
    "?": questionMark,
    "!": exclamationMark,
}

"""
Stores the data for new characters
This dictionary is used with the ch dictionary
Format: 
    "Name of the character": A string that has the 
"""
additionalChr = {}

"""
This dictionary contains the possible movements of the turtle when operated by the user
"""
moveTrt = {
    "W": moveForward,
    "S": moveBackwards,
    "A": rotateLeft,
    "D": rotateRight,
    "G": moveDown,
    "F": moveUp
}

"""
This is the string versions of the dictionary moveTrt
"""
moveTrtName = {
    "W": "forward",
    "S": "backwards",
    "A": "rotateLeft",
    "D": "rotateRight",
    "G": "moveDown",
    "F": "moveUp"
}

"""
This dictionary is used to create a bond between the command that needs to be executed and what is read from the file
"""
moveTrtInterpretation = {
    "forward": moveForward,
    "backwards": moveBackwards,
    "rotateLeft": rotateLeft,
    "rotateRight": rotateRight,
    "moveDown": moveDown,
    "moveUp": moveUp
}
