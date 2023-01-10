import functools
from datetime import datetime
from functools import reduce

from models.Identifiable import Identifiable


class Order(Identifiable):
    def __init__(self, id_, customer_id, dish_ids=None, drinks_ids=None, costs=0, time_stamp="0"):
        super().__init__(id_)
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.drinks_ids = drinks_ids
        self.costs = costs
        self.time_stamp = time_stamp if time_stamp != "0" else f"{datetime.now().hour}:{datetime.now().minute}"

    def __eq__(self, other):
        return self.customer_id == other.customer_id \
            and self.dish_ids == other.dish_ids \
            and self.drinks_ids == other.drinks_ids

    def __str__(self):
        return f"Customer Id: {self.customer_id}, Dish Ids: {self.dish_ids}, " \
               f" Drinks Ids: {self.drinks_ids}, costs: {self.costs}, Order Time: {self.time_stamp}"

    def __get_items(self, dishes, drinks):
        dish_list = list(filter(lambda dish: dish.id in self.dish_ids, dishes))
        drink_list = list(filter(lambda drink: drink.id in self.drinks_ids, drinks))
        return dish_list + drink_list

    def generate_costs(self, dishes, drinks):
        items_list = self.__get_items(dishes, drinks)
        costs = functools.reduce(lambda s, item: s + item.price, items_list, 0)
        return costs

    def generate_bill(self, dishes, drinks):
        items_list = self.__get_items(dishes, drinks)
        self.costs = self.generate_costs(dishes, drinks)
        bill_lines = list(map(lambda item: f"'{item.name}' ... '{item.price}'", items_list))
        bill_lines.append(f"Your bill is '{self.costs}' $ worth!")

        return reduce(lambda s1, s2: s1 + '\n' + s2, bill_lines)

    def show_bill(self, dishes, drinks):
        print(self.generate_bill(dishes, drinks))

    def __generate_estimated_time_for_preparation(self, dishes):
        dish_list = list(filter(lambda dish: dish.id in self.dish_ids, dishes))
        wait_time = sum(d.prep_time for d in dish_list)
        # print(wait_time)

        return  [wait_time // 60, wait_time % 60]

    def __generate_estimated_time_for_finishing_the_order(self, dishes):
        time = self.time_stamp.split(":")
        preparation_time = self.__generate_estimated_time_for_preparation(dishes)
        finished_time = [int(time[0]) + preparation_time[0], int(time[1]) + preparation_time[1]]

        return finished_time

    def generate_estimated_wait_time(self, dishes):
        time = self.time_stamp.split(":")
        finished_time = self.__generate_estimated_time_for_finishing_the_order(dishes)

        return f"{finished_time[0] - int(time[0])} : {finished_time[1] - int(time[1])}"
