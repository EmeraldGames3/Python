from Modelle.Kunde import Customer
from UI.For_Clients import *

customer_list = []


def add_customers():
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    customer_name = customer_name_1()
    adresse = adresse_1()
    customer = Customer(customer_name, adresse)
    customer_list.append(customer)
    customer_formatter.save(customer_list)


def update_customer_info():
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    customer_name = update_customer_name()
    update_customer_start()
    to_change = value_to_change()
    new_value = new_value_()

    match to_change:
        case 'name':
            for customer in range(0, len(customer_list)):
                if customer_list[customer].name == customer_name:
                    customer_list[customer].name = new_value
            customer_formatter.save(customer_list)

        case 'adresse':
            for customer in range(0, len(customer_list)):
                if customer_list[customer].name == customer_name:
                    customer_list[customer].adresse = new_value
            customer_formatter.save(customer_list)


def delet_customer():
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    customer_name = delet_customer_name()
    for idx, customer in enumerate(customer_list):
        if customer.name == customer_name:
            del customer_list[idx]
    customer_formatter.save(customer_list)


def show_customers():
    customer_database()


def customer_controller():
    print_on_screen()
    complete = False
    while not complete:
        option = for_option()
        match option:
            case 1:
                show_customers()
                answere = answere_customer_management()
                match answere:
                    case 'yes':
                        customer_controller()
                    case 'no':
                        complete = True

            case 2:
                add_customers()
                complete_ad = False
                while complete_ad is False:
                    answere1 = for_answere_add_item()
                    match answere1:
                        case 'yes':
                            add_customers()
                        case 'no':
                            complete_ad = True
                answere = answere_customer_management()
                match answere:
                    case 'yes':
                        customer_controller()
                    case 'no':
                        complete = True

            case 3:
                update_customer_info()
                complete_up = False
                while complete_up is False:
                    answere2 = for_answere_update_item()
                    match answere2:
                        case 'yes':
                            add_customers()
                        case 'no':
                            complete_up = True
                answere = answere_customer_management()
                match answere:
                    case 'yes':
                        customer_controller()
                    case 'no':
                        complete = True
            case 4:
                delet_customer()
                complete_del = False
                while complete_del is False:
                    answere3 = for_answere_delet_item()
                    match answere3:
                        case 'yes':
                            delet_customer()
                        case 'no':
                            complete_del = True
                answere = answere_customer_management()
                match answere:
                    case 'yes':
                        customer_controller()
                    case 'no':
                        complete = True

    print("Changes were made succesfully")
