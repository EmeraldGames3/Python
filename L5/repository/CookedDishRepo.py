from functools import reduce

from models.CookedDish import CookedDish
from repository.DataRepo import DataRepo


class CookedDishRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convertToString(self, dishes):
        strList = list(map(lambda item: f"{item.id},{item.name},{item.portionSize},{item.price},{item.prepTime}", dishes))
        return reduce(lambda s1, s2: s1 + '\n' + s2, strList)

    def convertFromString(self, string: str):
        if string == "":
            return []

        def lineToDish(line):
            params = line.split(',')
            return CookedDish(int(params[0]), params[1], int(params[2]), int(params[3]), int(params[4]))

        lines = string.split('\n')
        return list(map(lambda line: lineToDish(line), lines))
