from functools import reduce

from models.ID import ID


class Bestellung(ID):
    def __init__(self, id_: int, customerID: int, dishIDs: list[int], drinksIDs: list[int], costs = None,timeStamp = ""):
        super().__init__(id_)
        self.timeStamp = timeStamp
        self.drinksIDs = drinksIDs
        self.dishIDs = dishIDs
        self.customerID = customerID
        # TODO: Make this work
        # self.costs = self.generate_costs() if costs is None else costs


    def __get_items(self, dishes, drinks):
        dish_list = list(filter(lambda dish: dish.id in self.dishIDs, dishes))
        drink_list = list(filter(lambda drink: drink.id in self.drinksIDs, drinks))
        return dish_list + drink_list

    def generate_costs(self, dishes, drinks):
        items_list = self.__get_items(dishes, drinks)
        costs = reduce(lambda s, item: s + item.price, items_list, 0)
        return costs

    def generate_bill(self, dishes, drinks):
        items_list = self.__get_items(dishes, drinks)
        self.costs = self.generate_costs(dishes, drinks)
        bill_lines = list(map(lambda item: f"'{item.name}' ... '{item.price}'", items_list))
        bill_lines.append(f"\nYour bill is '{self.costs}' $ worth!")

        return reduce(lambda s1, s2: s1 + '\n' + s2, bill_lines)

    def show_bill(self, dishes, drinks):
        print(self.generate_bill(dishes, drinks))

