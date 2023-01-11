from Controller.Clients import *
from Modelle.Bestellung import Order
from UI.For_Order import *


def show_orders():
    """
    print on screen all orders

    """
    for_show_order()


def remove_order():
    """

    steps: show all orders to see the id of the order you would like to remove
    """
    show_orders()
    order_formatter = OrderFormatter('../Files/Order_Database')
    order_list = order_formatter.load()
    order_id = enter_id()
    for idx, order in enumerate(order_list):
        if order.id == order_id:
            del order_list[idx]
    order_formatter.save(order_list)


def select_customer():
    """

    :return: the customer you chose through a specific method:
    simply select a customer from a list
    select a customer by search
    create a new customer
    """
    print_on_screen_select()

    option = for_option()
    match option:
        case 1:
            return select_customer_from_list()

        case 2:
            return select_customer_by_search()

        case 3:
            return select_new_customer()


def select_customer_from_list():
    """
    steps: show the customers list and choose the number of the customer you want
    :return: customer
    """
    show_customers()
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    customer_number = choose_customer_number()
    customer = customer_list[customer_number - 1]
    return customer


def select_customer_by_search():
    """
    steps:
            Choose name/or address as a criteria
            Get a filtered list of objects that contain the entered name/address
            Choose from the filtered list the wanted customer
    :return: customer
    """
    customer = Customer()
    criteria()
    opt = for_option()
    match opt:
        case 1:
            name = input("Name= ")
            customer.name = name

        case 2:
            address = input("Address= ")
            customer.address = address

    filtered = search(customer)
    show_results_after_search(filtered)
    option = for_option()
    return filtered[option - 1]


def select_new_customer():
    """
    create new customer and add it to Customer_Database
    :return: customer
    """
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    customer_name = customer_name_1()
    adresse = adresse_1()
    customer = Customer(customer_name, adresse)
    customer_list.append(customer)
    customer_formatter.save(customer_list)
    return customer


def add_order():
    """
    steps:
            select the customer and get id
            select drinks and get ids
            select dishes and get ids
            save the order to 'Order_Database' file
    """
    order_formatter = OrderFormatter('../Files/Order_Database')
    order_list = order_formatter.load()
    customer = select_customer()
    customer_id = customer.id
    drink_order = select_drinks()
    dish_order = select_dishes()
    drinks_ids = list(map(lambda drink: drink.id, drink_order))
    dishes_ids = list(map(lambda dish: dish.id, dish_order))
    new_order = Order(customer_id, drinks_ids, dishes_ids)
    order_list.append(new_order)
    order_formatter.save(order_list)


def order_controller():
    print_on_screen()
    complete = False
    while not complete:
        option = for_option()
        match option:
            case 1:
                show_orders()
                answere = answere_menu()
                match answere:
                    case 'yes':
                        order_controller()
                    case 'no':
                        complete = True

            case 2:
                add_order()
                answere = answere_menu()
                match answere:
                    case 'yes':
                        order_controller()
                    case 'no':
                        complete = True

            case 3:
                remove_order()
                answere = answere_menu()
                match answere:
                    case 'yes':
                        order_controller()
                    case 'no':
                        complete = True

