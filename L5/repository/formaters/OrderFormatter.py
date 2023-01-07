import pickle

from repository.formaters.DataFormatter import DataFormatter


class OrderFormatter(DataFormatter):
    def __init__(self, file):
        super().__init__(file)

    def convertToString(self, order_list):
        return pickle.dumps(order_list)

    def convertFromString(self, string):
        return [] if len(string) == 0 else pickle.loads(string)
