from Controller.Clients import *


def update_customer_name_test():
    show_customers()
    customer_formatter = CustomerFormatter('../Files/Customer_Database')
    customer_list = customer_formatter.load()
    customer_name = input('Choose customer: ')
    customer_updated_name = input('New name: ')
    for customer in range(0, len(customer_list)):
        if customer_list[customer].name == customer_name:
            customer_list[customer].name = customer_updated_name
    customer_formatter.save(customer_list)
    show_customers()

update_customer_name_test()
