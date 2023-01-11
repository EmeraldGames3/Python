from Controller.Menu import *


def add_drink_test():
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    drink = Getrank('Sprite', '0%', '200 ml', 10)
    drinks_liste.append(drink)
    drink_formatter.save(drinks_liste)
    added_drink = drink_formatter.load()[-1]
    attribute_dict = added_drink.__dict__
    for attribute in attribute_dict:
        if drink.__getattribute__(attribute) != added_drink.__getattribute__(attribute):
            return False
    return True


def add_dish_test():
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    dish = Gekochter_Gericht('Lasagna', '20 Minuten', '200g', 30)
    gericht_liste.append(dish)
    cooked_dish_formatter.save(gericht_liste)
    added_dish = cooked_dish_formatter.load()[-1]
    attribute_dict = added_dish.__dict__
    for attribute in attribute_dict:
        if dish.__getattribute__(attribute) != added_dish.__getattribute__(attribute):
            return False
    return True


def main():
    print(add_drink_test())
    print(add_dish_test())


main()
