import hashlib

from models.ID import ID


class Customer(ID):
    def __init__(self, id_: int, name: str, address: str):
        super().__init__(id_)
        self.__name = name
        self.__address = address