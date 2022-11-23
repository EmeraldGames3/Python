def printChoices():
    """
    Here we print to the player the possible choices
    """
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print()


"""
Animations
"""
optAnimations = {

}


def addAnimations():
    aux = []
    with(open("ex3.txt") as f):
        for line in f:
            aux.append(line.strip("\n"))

    optAnimations["Rock"] = ""
    optAnimations["Paper"] = ""
    optAnimations["Scissors"] = ""

    # print(aux)

    # print(optAnimations)

    for i in range(aux.index("Rock"), aux.index("Paper")):
        optAnimations["Rock"] += (aux[i] + "\n")

    for i in range(aux.index("Paper"), aux.index("Scissors")):
        optAnimations["Rock"] += (aux[i] + "\n")

    for i in range(len(aux)):
        optAnimations["Rock"] += (aux[i] + "\n")

    # print(optAnimations)
