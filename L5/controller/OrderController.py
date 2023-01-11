from models.Customer import Customer
from models.Dish import Dish
from models.Drink import Drink
from models.Order import Order


def add_order(orders: list[Order], dishes: list[Dish], drinks: list[Drink], customers: list[Customer]):
    """
    :param orders: A list of all orders
    :param dishes: A list of all dishes
    :param drinks: A list of all drinks
    :param customers: A list of all customers
    This function handles everything there is about orders
    """

