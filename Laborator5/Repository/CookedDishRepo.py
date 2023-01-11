from Modelle.GekochterGericht import Gekochter_Gericht
from Repository.DataRepo import DataFormatter


class CookedDishFormatter(DataFormatter):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__(file_name)

    def convert_to_string(self, cooked_dish_list):
        string = '\n'.join(map(str, cooked_dish_list))
        return string

    def do(self, dish):
        obj = Gekochter_Gericht(dish[1], dish[2], dish[3], int(dish[4]))
        obj.id = int(dish[0])
        return obj

    def convert_from_string(self, content):
        liste = content.split('\n')
        liste_2 = list(map(lambda string: string.split(','), liste))
        rez = list(map(self.do, liste_2))
        return rez
