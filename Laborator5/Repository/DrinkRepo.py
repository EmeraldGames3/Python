from Modelle.Getränk import Getrank
from Repository.DataRepo import DataFormatter


class DrinkFormatter(DataFormatter):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__(file_name)

    def convert_to_string(self, drink_list):
        string = '\n'.join(map(str, drink_list))
        return string

    def do(self, drink):
        obj = Getrank(drink[1], drink[2], drink[3], int(drink[4]))
        obj.id = int(drink[0])
        return obj

    def convert_from_string(self, content):
        liste = content.split('\n')
        liste_2 = list(map(lambda string: string.split(','), liste))
        rez = list(map(self.do, liste_2))
        return rez
