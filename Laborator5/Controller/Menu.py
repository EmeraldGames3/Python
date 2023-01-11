from Modelle.GekochterGericht import Gekochter_Gericht
from Modelle.Getränk import Getrank
from UI.For_Menu import *

drinks_liste = []
gericht_liste = []


def add_drink():
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    drink_name = drink_name_1()
    alkoholgehalt = alkoholgehalt_1()
    portionsgrosse = portionsgrosse_1()
    preis = preis_1()
    drink = Getrank(drink_name, alkoholgehalt, portionsgrosse, preis)
    drinks_liste.append(drink)
    drink_formatter.save(drinks_liste)


def add_dish():
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    gericht_name = dish_name_1()
    zubereitungszeit = zubereitungszeit_1()
    portionsgrosse = portionsgrosse_1()
    preis = preis_1()
    gericht = Gekochter_Gericht(gericht_name, zubereitungszeit, portionsgrosse, preis)
    gericht_liste.append(gericht)
    cooked_dish_formatter.save(gericht_liste)


def add_item():
    start_for_add_item()
    menu_complete = False
    while not menu_complete:
        option = for_option()
        match option:
            case 1:
                add_drink()
                answere = for_answere_add_item()
                match answere:
                    case 'yes':
                        add_item()
                    case 'no':
                        menu_complete = True
            case 2:
                add_dish()
                answere = for_answere_add_item()
                match answere:
                    case 'yes':
                        add_item()
                    case 'no':
                        menu_complete = True


def update_drink():
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    drink_name = update_drink_name()
    update_drink_start()
    to_change = value_to_change()
    if to_change != 'preis':
        new_value = new_value_()
    else:
        new_value = int(new_value_())

    match to_change:
        case 'name':
            for drink in range(0, len(drinks_liste)):
                if drinks_liste[drink].name == drink_name:
                    drinks_liste[drink].name = new_value
            drink_formatter.save(drinks_liste)

        case 'alkoholgehalt':
            for drink in range(0, len(drinks_liste)):
                if drinks_liste[drink].name == drink_name:
                    drinks_liste[drink].alkoholgehalt = new_value
            drink_formatter.save(drinks_liste)

        case 'portionsgrosse':
            for drink in range(0, len(drinks_liste)):
                if drinks_liste[drink].name == drink_name:
                    drinks_liste[drink].portionsgrosse = new_value
            drink_formatter.save(drinks_liste)

        case 'preis':
            for drink in range(0, len(drinks_liste)):
                if drinks_liste[drink].name == drink_name:
                    drinks_liste[drink].preis = new_value
            drink_formatter.save(drinks_liste)


def update_dish():
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    dish_name = update_dish_name()
    update_dish_start()
    to_change = value_to_change()
    if to_change != 'preis':
        new_value = new_value_()
    else:
        new_value = int(new_value_())

    match to_change:
        case 'name':
            for dish in range(0, len(gericht_liste)):
                if gericht_liste[dish].name == dish_name:
                    gericht_liste[dish].name = new_value
            cooked_dish_formatter.save(gericht_liste)

        case 'zubereitungszeit':
            for dish in range(0, len(gericht_liste)):
                if gericht_liste[dish].name == dish_name:
                    gericht_liste[dish].zubereitungszeit = new_value
            cooked_dish_formatter.save(gericht_liste)
        case 'portionsgrosse':
            for dish in range(0, len(gericht_liste)):
                if gericht_liste[dish].name == dish_name:
                    gericht_liste[dish].portionsgrosse = new_value
            cooked_dish_formatter.save(gericht_liste)

        case 'preis':
            for dish in range(0, len(gericht_liste)):
                if gericht_liste[dish].name == dish_name:
                    gericht_liste[dish].preis = new_value
            cooked_dish_formatter.save(gericht_liste)


def update_item():
    update_item_start()
    complete = False
    while not complete:
        option = for_option()
        match option:
            case 1:
                update_drink()
                answere = for_answere_update_item()
                match answere:
                    case 'yes':
                        update_item()
                    case 'no':
                        complete = True
            case 2:
                update_dish()
                answere = for_answere_update_item()
                match answere:
                    case 'yes':
                        update_item()
                    case 'no':
                        complete = True


def delete_dish():
    cooked_dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    gericht_liste = cooked_dish_formatter.load()
    dish_name = delet_dish_name()
    for idx, dish in enumerate(gericht_liste):
        if dish.name == dish_name:
            del gericht_liste[idx]

    cooked_dish_formatter.save(gericht_liste)


def delete_drink():
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks_liste = drink_formatter.load()
    drink_name = delet_drink_name()
    for idx, drink in enumerate(drinks_liste):
        if drink.name == drink_name:
            del drinks_liste[idx]

    drink_formatter.save(drinks_liste)


def delete_item():
    delete_item_start()
    complete = False
    while not complete:
        option = for_option()
        match option:
            case 1:
                delete_drink()
                answere = for_answere_delete_item()
                match answere:
                    case 'yes':
                        delete_item()
                    case 'no':
                        complete = True
            case 2:
                delete_dish()
                answere = for_answere_delete_item()
                match answere:
                    case 'yes':
                        delete_item()
                    case 'no':
                        complete = True


def show_food_menu():
    for_show_food_menu()


def show_drinks_menu():
    for_show_drink_menu()


def show_menu():
    show_drinks_menu()
    show_food_menu()


def menu_controller():
    print_on_screen()
    complete = False
    while not complete:
        option = for_option()
        match option:
            case 1:
                show_menu()
                answere = answere_menu()
                match answere:
                    case 'yes':
                        menu_controller()
                    case 'no':
                        complete = True

            case 2:
                add_item()
                answere = answere_menu()
                match answere:
                    case 'yes':
                        menu_controller()
                    case 'no':
                        complete = True

            case 3:
                update_item()
                answere = answere_menu()
                match answere:
                    case 'yes':
                        menu_controller()
                    case 'no':
                        complete = True
            case 4:
                delete_item()
                answere = answere_menu()
                match answere:
                    case 'yes':
                        menu_controller()
                    case 'no':
                        complete = True
