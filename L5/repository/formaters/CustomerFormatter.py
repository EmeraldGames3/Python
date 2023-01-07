import pickle

from repository.formaters.DataFormatter import DataFormatter


class CustomerFormatter(DataFormatter):
    def __init__(self, file):
        super().__init__(file)

    def convertToString(self, customer_list):
        return pickle.dumps(customer_list)

    def convertFromString(self, string):
        return [] if len(string) == 0 else pickle.loads(string)
