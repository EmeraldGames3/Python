"""
This dictionary contains the possible outcomes of a rock paper scissors game
"""
outcomes = {
    1: "Player wins",
    2: "Computer wins",
    3: "Draw"
}

"""
This tuple stores the three possible options of the game
"""
opt = (
    "Rock",
    "Paper",
    "Scissors"
)


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
