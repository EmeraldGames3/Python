from models.Customer import Customer
from repository.CustomerRepo import CustomerRepo


def add_new_customer(customerRepo: CustomerRepo):
    print("A customer has the following attributes: a name and an address")
    name = input("Name: ")
    address = input("Address: ")