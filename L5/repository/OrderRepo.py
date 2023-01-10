from functools import reduce

from models.Order import Order
from repository.DataRepo import DataRepo


class OrderRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, obj_list):
        str_list = \
            map(lambda item: f"{item.id},{item.customer_id},{list_to_string(item.dish_ids)},"
                             f"{list_to_string(item.drinks_ids)},{item.costs},{item.time_stamp}", obj_list)
        return reduce(lambda s1, s2: s1 + '\n' + s2, str_list)

    def convert_from_string(self, string):
        if string == "":
            return []

        def line_to_dash(line):
            params: list[str] = line.split(',')

            dish_str = params[2].strip("[]")
            dishes = [] if dish_str == "" else list(map(lambda dish: int(dish), dish_str.split(';')))

            drink_str = params[3].strip("[]")
            drinks = [] if drink_str == "" else list(map(lambda dish: int(dish), drink_str.split(';')))

            return Order(int(params[0]), int(params[1]), dishes, drinks, int(params[4]), params[5])

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))


def list_to_string(lst):
    string = "["
    for el in lst:
        string += str(el) + ';'
    string = string[:-1]
    return string + ']'
