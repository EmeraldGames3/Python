from ex1.data import moveTrt


def printOptions():
    print("Enter 1 to write a word")
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
