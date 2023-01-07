import pickle

from repository.formaters.DataFormatter import DataFormatter


class CookedDishFormatter(DataFormatter):
    def __init__(self, file=None):
        super().__init__(file)

    def convertToString(self, cooked_dish_list):
        return pickle.dumps(cooked_dish_list)

    def convertFromString(self, string):
        return [] if len(string) == 0 else pickle.loads(string)
