from GUI import printGUI
from IO import readLetter, writeToFile
from gameLogik import gameSetUp, hasLost, hasWon, constructHiddenWord

word, hiddenWord, wordList = gameSetUp()


def gameLoop(lives):
    global hiddenWord
    while True:
        printGUI(lives, hiddenWord)

        if hasLost(lives):
            writeToFile("content.txt", "You lost")
            break

        ch = readLetter()

        if ch not in wordList:
            wordList[ch] = 1
            writeToFile("content.txt", ch + "\n")
            hiddenWord, lives = constructHiddenWord(ch, word, hiddenWord, lives)

        else:
            print("This letter was already chosen")

        if hasWon(hiddenWord, word):
            writeToFile("content.txt", "You won")
            break


gameLoop(5)
