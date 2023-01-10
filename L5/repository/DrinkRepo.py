from functools import reduce
from models.Drink import Drink
from repository.DataRepo import DataRepo


class DrinkRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convertToString(self, drinks):
        strList = map(lambda item: f"{item.id_},{item.name},{item.portion_size},{item.price},{item.alcohol}", drinks)
        return reduce(lambda s1, s2: s1 + '\n' + s2, strList)

    def convertFromString(self, string):
        if string == "":
            return []

        def lineToDash(line):
            params = line.split(',')
            return Drink(int(params[0]), params[1], int(params[2]), int(params[3]), int(params[4]))

        lines = string.split('\n')
        return map(lambda line: lineToDash(line), lines)
