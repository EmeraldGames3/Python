from Modelle.Kunde import Customer
from Repository.DataRepo import DataFormatter


class CustomerFormatter(DataFormatter):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__(file_name)

    def convert_to_string(self, customer_list):
        string = '\n'.join(map(str, customer_list))
        return string

    def do(self, kunde):
        obj = Customer(kunde[1], kunde[2])
        obj.id = int(kunde[0])
        return obj

    def convert_from_string(self, content):
        liste = content.split('\n')
        liste_2 = list(map(lambda string: string.split(','), liste))
        rez = list(map(self.do, liste_2))
        return rez
