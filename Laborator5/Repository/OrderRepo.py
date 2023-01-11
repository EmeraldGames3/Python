from Modelle.Bestellung import Order
from Repository.DataRepo import DataFormatter


class OrderFormatter(DataFormatter):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__(file_name)

    def convert_to_string(self, order_list):
        string = '\n'.join(map(str, order_list))
        return string

    def do(self, attr):
        obj = Order(int(attr[1]), list(map(int, attr[2][1:len(attr[2]) - 1].split(','))),
                    list(map(int, attr[3][1:len(attr[3]) - 1].split(','))))
        obj.id = int(attr[0])
        return obj

    def convert_from_string(self, content):
        liste = content.split('\n')
        liste_2 = list(map(lambda string: string.split(' || '), liste))
        rez = list(map(self.do, liste_2))
        return rez
