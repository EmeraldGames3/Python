from functools import reduce


class Menu:
    def __init__(self, dishes, drinks):
        self.drinks = drinks
        self.dishes = dishes

    def __generate_menu(self):
        menu_lines = list(map(lambda item: f"'{item.name}'...'{item.price}", self.dishes + self.drinks))
        return reduce(lambda s1, s2: s1 + "\n" + s2, menu_lines)

    def __str__(self):
        return self.__generate_menu()