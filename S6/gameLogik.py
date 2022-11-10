from IO import clearFile, writeToFile


def constructHiddenWord(ch, word, hiddenWord, lives):
    if ch in word:
        hiddenWord = reconstructHiddenWord(ch, word, hiddenWord)
    else:
        lives -= 1

    return hiddenWord, lives


def reconstructHiddenWord(ch, word, hiddenWord):
    indexes = []
    for i in range(len(word)):
        if word[i] == ch:
            indexes += [i]

    for i in indexes:
        hiddenWord = hiddenWord[:i] + ch + hiddenWord[i + 1:]

    return hiddenWord


def gameSetUp():
    word = input("Word to be guessed: ")
    hiddenWord = "*" * len(word)
    wordList = {}

    clearFile("content.txt")
    writeToFile("content.txt", f"{word} \n")

    return word, hiddenWord, wordList


def hasLost(lives):
    if lives == 0:
        print("You lost")
        return True
    return False


def hasWon(hiddenWord, word):
    if hiddenWord == word:
        print(f"Your word was {word}")
        print("Congratulations")
        print("You won")
        return True

    return False
