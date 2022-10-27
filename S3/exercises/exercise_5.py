from exercises import exercise_2


def biggerStringSum(s1, s2):
    filler = "0" * abs((len(s1) - len(s2)))

    if s1 > s2:
        s2 = filler + s2
    else:
        s1 = filler + s1

    return exercise_2.bigStringSum(s1, s2)
