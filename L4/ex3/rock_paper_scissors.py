import random


def printChoices():
    """
    Here we print to the player the possible choices
    """
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print()


"""
This dictionary stores the three possible options of the game
"""
opt = (
    "Rock",
    "Paper",
    "Scissors"
)

"""
This dictionary contains the possible outcomes of a rock paper scissors game
"""
outcomes = {
    1: "Player wins",
    2: "Computer wins",
    3: "Draw"
}


def gameLogic(playerOption, computerOption):
    """
    This functions contains all the logic of the rock paper scissors game
    :return: A number that is in the outcomes dictionary
    """
    if computerOption == playerOption:
        return 3

    match playerOption:
        case 1:
            """
            This means that the player has chosen rock
            """
            if computerOption == 2:
                return 2
            return 1

        case 2:
            """
            This means that the player has chosen paper
            """
            if computerOption == 3:
                return 2
            return 1

        case 3:
            """
            This means that the player has chosen scissors
            """
            if computerOption == 1:
                return 2
            return 1


def playGame():
    """"
    This functions contains the actual game
    The overall game finishes once three games of rock paper scissors have been played
    A draw does not count towards the number of played games
    """
    gameNumber = 0
    playerScore = 0
    computerScore = 0

    print()

    while gameNumber < 3:
        print(f"Your score is {playerScore}")
        print(f"The computers score is {computerScore}")
        printChoices()

        playerOption = int(input("Enter your Choice ").strip())
        if playerOption not in range(1, 4):
            print("Invalid option")
            continue

        computerOption = random.choice(opt)
        print(f"The computer has played {computerOption}")

        computerOption = opt.index(computerOption) + 1

        outcome = gameLogic(playerOption, computerOption)

        print(outcomes[outcome])

        # 1 means that the player won
        # 2 means that the computer won
        # 3 means that it was a draw
        if outcome == 1:
            playerScore += 1
            gameNumber += 1
        elif outcome == 2:
            computerScore += 1
            gameNumber += 1

    if computerScore > playerScore:
        print("The computer has bested you")
    else:
        print("Good job soldier you have defeated the machines")
