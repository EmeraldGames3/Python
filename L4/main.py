from ex3.rock_paper_scissors import playGame
from ex2.change_words import call_changeWords
from ex1.write_turtle import writeToTurtle

"""
This dictionary is used to create a menu for the overall homework
"""
ex = {
    "1": writeToTurtle,
    "2": call_changeWords,
    "3": playGame,
}


def printOptions():
    print("1. Draw letters")
    print("2. Change words")
    print("3. Rock, paper, scissors")
    print("If you press an invalid key the program ends")


def run():
    """
    This function is used to check a specific exercise
    You choose witch exercise you want to see or choose any other number if you want to exit
    """
    while True:
        printOptions()

        option = input("Your option: ").strip()

        if option in ex:
            ex[option]()
            print()
        else:
            print("Invalid option")
            break


run()