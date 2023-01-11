from Controller.Menu import show_drinks_menu, show_food_menu
from Modelle.Needed_dict import name_id_drink, name_id_dish
from Repository.CookedDishRepo import CookedDishFormatter
from Repository.CustomerRepo import CustomerFormatter
from Repository.DrinkRepo import DrinkFormatter
from Repository.OrderRepo import OrderFormatter


def for_show_order():
    order_formatter = OrderFormatter('../Files/Order_Database')
    order_list = order_formatter.load()
    drinks_dict = name_id_drink()
    dish_dict = name_id_dish()

    print()
    print()
    print("                                                 ALL ORDERS                          ")
    print()
    print()

    for order in order_list:
        list_dish = list(map(lambda id_: dish_dict[id_], order.liste_id_dish))
        list_drink = list(map(lambda id_: drinks_dict[id_], order.liste_id_drinks))
        print("ID Order: ", order.id, "||  ID Customer: ", order.kunde_id, "||  Drinks: ", list_drink, "||  Dish: ",
              list_dish)
    print()
    print()


def answere_menu():
    answere = input("Is there any other operation regarding orders that you would like to perform?: yes/no ")
    return answere


def for_option():
    option = int(input("Choose the corresponding number: "))
    return option


def enter_id():
    order_id = int(input("Enter the id: "))
    return order_id


def print_on_screen():
    print()
    print()
    print("                                                              ORDER DATABASE                        ")
    print()
    print()
    print("Choose one of the following options:")
    print("                                     ")
    print("                                     1. View all orders ")
    print("                                     ")
    print("                                     2. Add a new order ")
    print("                                     ")
    print("                                     3. Remove order ")
    print("                                     ")


def print_on_screen_select():
    print()
    print()
    print("                                                              ORDER DATABASE                        ")
    print()
    print()
    print("Choose one of the following options:")
    print("                                     ")
    print("                                     1. Select customer from list ")
    print("                                     ")
    print("                                     2. Select customer by search ")
    print("                                     ")
    print("                                     3. Add new customer ")
    print("                                     ")


def choose_customer_number():
    option = int(input("Choose the corresponding number: "))
    return option


def criteria():
    print('Search customer by: 1. Name || 2. Address')


def select_drinks():
    """

    :return: a list of drinks chosen by the customer
    """
    drink_formatter = DrinkFormatter('../Files/Speisekarte_Drink')
    drinks = drink_formatter.load()
    show_drinks_menu()
    drinks_order = []
    print("Select drinks from the menu")
    done = False
    while not done:
        drink_name = input("Choose drink: ")
        for drink in drinks:
            if drink.name == drink_name:
                drinks_order.append(drink)
        answere = input("Is that all? (yes/ no)")
        match answere:
            case 'yes':
                done = True
            case 'no':
                done = False

    return drinks_order


def select_dishes():
    dish_formatter = CookedDishFormatter('../Files/Speisekarte_Dish')
    dishes = dish_formatter.load()
    show_food_menu()
    dishes_order = []
    print("Select dishes from the menu")
    done = False
    while not done:
        dish_name = input("Choose dish: ")
        for dish in dishes:
            if dish.name == dish_name:
                dishes_order.append(dish)
        answere = input("Is that all? (yes/ no)")
        match answere:
            case 'yes':
                done = True
            case 'no':
                done = False

    return dishes_order


def search(customer):
    """

    :param customer: object - Customer Class
    :return:  filterd list objects that contain a part of the name/address
    """
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    # name_attr = dir(customer_list[0])[-1] => 'name'
    # address_attr = dir(customer_list[0])[-3] => 'adresse'
    if customer.name is not None:
        filtered = list(
            filter(lambda customer1: customer.name.lower() in getattr(customer1, 'name').lower(), customer_list))
        return filtered
    if customer.adresse is not None:
        filtered = list(
            filter(lambda customer1: customer.adresse.lower() in getattr(customer1, 'adresse').lower(), customer_list))
        return filtered
    return False

def show_results_after_search(filtered):
    for i, element in enumerate(filtered, 1):
        print(i, '.', element)



