def extractFile(fileName):
    """
    This function is used to extract the contents of a file in variable
    :param fileName: The name of the file to be accessed
    :return: A list that contains the contents of the file
    """

    l = []

    with(open(fileName) as file):
        for line in file:
            l.append(line.strip())

    return l


def changeWords(word, filename):
    """
    Thist function changes all occureces of a word in the list
    :param word:
    :param filename: the name of the file
    """
    pass


def changeWordsInFile(fileName):
    """
    :param fileName: The name of the file
    The specified file will be changed according to the changes in the list
    """
    pass


def call_changeWords():
    fl = "ex2.txt"
    try:
        fileText = extractFile(fl)
    except FileNotFoundError as ex:
        print(ex)
        return

    option = input("Enter word to be replaced ").strip()
    changeWords(option, fl)
