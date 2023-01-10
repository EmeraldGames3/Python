import hashlib

from models.Dish import Dish


class Drink(Dish):
    def __init__(self, id_: int = None, name=None, portion_size: int = None, price: int = None,
                 alcohol_content: int = None):
        super().__init__(id_, name, portion_size, price)
