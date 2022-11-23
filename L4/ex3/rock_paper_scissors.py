import random

from ex3.IO import printChoices, optAnimations, addAnimations
from ex3.logik import gameLogic, outcomes, opt


def playGame():
    """"
    This functions contains the actual game
    The overall game finishes once three games of rock paper scissors have been played
    A draw does not count towards the number of played games
    """

    addAnimations()

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

        print(optAnimations[opt[playerOption - 1]])

        computerOption = random.choice(opt)
        print(f"The computer has played {computerOption}")
        print(optAnimations[computerOption])

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
