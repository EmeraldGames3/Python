import pickle

from repository.formaters.DataFormatter import DataFormatter


class DrinkFormatter(DataFormatter):
    def __init__(self, file=None):
        super().__init__(file)

    def convertToString(self, drink_list):
        return pickle.dumps(drink_list)

    def convertFromString(self, string):
        return [] if len(string) == 0 else pickle.loads(string)
