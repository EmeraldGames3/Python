from Repository.CookedDishRepo import CookedDishFormatter
from Repository.DrinkRepo import DrinkFormatter


def menu_dict_speise():
    menu_dict = {}
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    for i in range(len(gericht_liste)):
        menu_dict[gericht_liste[i].id] = gericht_liste[i]

    return menu_dict


def name_id_dish():
    menu_dict = {}
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    for i in range(len(gericht_liste)):
        menu_dict[gericht_liste[i].id] = gericht_liste[i].name

    return menu_dict


def menu_preis_dict_speise():
    menu_preis_dict = {}
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    for i in range(len(gericht_liste)):
        menu_preis_dict[gericht_liste[i].id] = gericht_liste[i].preis
        # in loc de 2 dictionare as vrea sa am unul singur
        # menu_preis_dict[gericht_liste[i].id] = gericht_liste[i]
        # si abia cand lucrez cu el sa ii dau gerich_liste[i].preis

    return menu_preis_dict


def menu_dict_drinks():
    menu_dict = {}
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    for i in range(len(drinks_liste)):
        menu_dict[drinks_liste[i].id] = drinks_liste[i]

    return menu_dict


def name_id_drink():
    menu_dict = {}
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    for i in range(len(drinks_liste)):
        menu_dict[drinks_liste[i].id] = drinks_liste[i].name

    return menu_dict


def menu_preis_dict_drinks():
    menu_preis_dict = {}
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    for i in range(len(drinks_liste)):
        menu_preis_dict[drinks_liste[i].id] = drinks_liste[i].preis

    return menu_preis_dict
