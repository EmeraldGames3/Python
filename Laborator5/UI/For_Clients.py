from Repository.CustomerRepo import CustomerFormatter


def customer_name_1():
    customer_name = input("Enter the name of the customer: ")
    return customer_name


def adresse_1():
    adresse = input("Adress: ")
    return adresse


def for_answere_add_item():
    answere = input("Would you like to continue adding customers to your database?: yes/no ")
    return answere


def for_option():
    option = int(input("Choose the corresponding number: "))
    return option


def update_customer_name():
    drink_name = input("Enter the name of the customer: ")
    return drink_name


def update_customer_start():
    print("What would you like to update? ")
    print("name / adresse?")


def value_to_change():
    to_change = input("Write your answere here: ")
    return to_change


def new_value_():
    new_value = input("New value: ")
    return new_value


def for_answere_update_item():
    answere = input("Would you like to continue updating customer's info?: yes/no ")
    return answere


def delet_customer_name():
    customer_name = input("Enter the name of the customer: ")
    return customer_name


def for_answere_delet_item():
    answere = input("Would you like to continue deleting customers?: yes/no ")
    return answere


def customer_database():
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    ct = 1
    print()
    print()
    print("                                                 CUSTOMER DATABASE                          ")
    print()
    print()
    for customer in range(len(customer_list)):
        print(ct, ".  ", "Name: ", customer_list[customer].name, "||  Adresse: ", customer_list[customer].adresse)
        ct = ct + 1
    print()
    print()


def print_on_screen():
    print()
    print()
    print("                                                              HOMEPAGE                        ")
    print()
    print()
    print("Choose one of the following options:")
    print("                                     ")
    print("                                     1. View all the clients from the database")
    print("                                     ")
    print("                                     2. Add a new client to the database")
    print("                                     ")
    print("                                     3. Update information about client ")
    print("                                     ")
    print("                                     4. Delet client from database")


def answere_customer_management():
    answere = input("Is there any other operation regarding the clients that you would like to perform?: yes/no ")
    return answere
