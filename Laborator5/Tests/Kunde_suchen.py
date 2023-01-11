from Repository.CustomerRepo import *
from Modelle.Kunde import *
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
def select_customer_by_search():
    """
    steps:
            Choose name/or address as a criteria
            Get a filtered list of objects that contain the entered name/address
            Choose from the filtered list the wanted customer
    :return: customer
    """
    customer = Customer()
    opt = int(input('1.Name/ 2. Address'))
    match opt:
        case 1:
            name = input("Name= ")
            customer.name = name

        case 2:
            address = input("Address= ")
            customer.adresse = address

    filtered = search(customer)
    show_results_after_search(filtered)
def show_results_after_search(filtered):
    for i, element in enumerate(filtered, 1):
        print(i, '.', element)
def main():
    select_customer_by_search()
main()