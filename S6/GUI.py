separator = "*=" * 30

loseAnimation = " / ---- \n |    O \n |  / | \ \n |    | \n |   / \ \n -----"
oneLifeAnimation = " / ---- \n |    O \n |  / | \ \n |    | \n | \n -----"
twoLivesAnimation = " / ---- \n |    O \n |  / | \ \n | \n | \n -----"
threeLivesAnimation = " / ---- \n |  O \n |  | \n | \n | \n -----"
fourLivesAnimation = " / ---- \n |  O \n | \n | \n | \n -----"
startingAnimation = " / ---- \n | \n | \n | \n | \n -----"

animation = {
    0: loseAnimation,
    1: oneLifeAnimation,
    2: twoLivesAnimation,
    3: threeLivesAnimation,
    4: fourLivesAnimation,
    5: startingAnimation
}


def printGUI(lives, hiddenWord):
    print(separator)
    print(f"Your word is {hiddenWord}")
    print(f"lives: {lives}")
    print(animation[lives])