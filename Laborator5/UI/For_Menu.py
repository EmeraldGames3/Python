from Repository.CookedDishRepo import CookedDishFormatter
from Repository.DrinkRepo import DrinkFormatter


def drink_name_1():
    drink_name = input("Getrank: ")
    return drink_name


def alkoholgehalt_1():
    alkoholgehalt = input("Alkoholgehalt: ")
    return alkoholgehalt


def portionsgrosse_1():
    portionsgrosse = input("Portionsgrosse: ")
    return portionsgrosse


def preis_1():
    preis = int(input("Preis: "))
    return preis


def dish_name_1():
    gericht_name = input("Gericht: ")
    return gericht_name


def zubereitungszeit_1():
    zubereitungszeit = input("Zubereitungszeit: ")
    return zubereitungszeit


def for_option():
    option = int(input("Choose the corresponding number: "))
    return option


def for_answere_add_item():
    answere = input("Would you like to continue adding items to your menu?: yes/no ")
    return answere


def start_for_add_item():
    print("What would you like to add to your menu? : ")
    print("                                           1. Drink")
    print("                                           2. Dish")


def update_drink_name():
    drink_name = input("Enter the name of the drink: ")
    return drink_name


def update_dish_name():
    dish_name = input("Enter the name of the dish: ")
    return dish_name


def update_drink_start():
    print("What would you like to update? ")
    print("name, alkoholgehalt, portionsgrosse oder preis")


def value_to_change():
    to_change = input("Write your answere here: ")
    return to_change


def new_value_():
    new_value = input("New value: ")
    return new_value


def update_dish_start():
    print("What would you like to update? ")
    print("name, zubereitungszeit, portionsgrosse oder preis")


def update_item_start():
    print("What part of your menu would you like to update? : ")
    print("                                           1. Drinks")
    print("                                           2. Dishes")


def for_answere_update_item():
    answere = input("Would you like to continue updating items?: yes/no ")
    return answere


def delet_dish_name():
    dish_name = input("Enter the name of the dish: ")
    return dish_name


def delet_drink_name():
    drink_name = input("Enter the name of the drink: ")
    return drink_name


def delete_item_start():
    print("From what part of your menu would you like to delet? : ")
    print("                                           1. Drinks")
    print("                                           2. Dishes")


def for_answere_delete_item():
    answere = input("Would you like to continue deleting items?: yes/no ")
    return answere


def for_show_food_menu():
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    print()
    print()
    print("                                                 FOOD MENU                          ")
    print()
    print()

    for dish in range(len(gericht_liste)):
        print("Name: ", gericht_liste[dish].name, "||  Zubereitungszeit: ", gericht_liste[dish].zubereitungszeit,
              "||  Portionsgrosse: ", gericht_liste[dish].portionsgrosse, "||  Preis: ", gericht_liste[dish].preis)
    print()
    print()


def for_show_drink_menu():
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    print()
    print()
    print("                                                 DRINKS MENU                          ")
    print()
    print()
    for drink in range(len(drinks_liste)):
        print("Name: ", drinks_liste[drink].name, "||  Alkoholgehalt: ", drinks_liste[drink].alkoholgehalt,
              "||  Portionsgrosse: ", drinks_liste[drink].portionsgrosse, "||  Preis: ", drinks_liste[drink].preis)
    print()
    print()


def print_on_screen():
    print()
    print()
    print("                                                              MENU // HOMEPAGE                        ")
    print()
    print()
    print("Choose one of the following options:")
    print("                                     ")
    print("                                     1. View the menu ")
    print("                                     ")
    print("                                     2. Add a new item to the menu ")
    print("                                     ")
    print("                                     3. Update information about item ")
    print("                                     ")
    print("                                     4. Delet item from menu")

def answere_menu():
    answere = input("Is there any other operation regarding the menu that you would like to perform?: yes/no ")
    return answere