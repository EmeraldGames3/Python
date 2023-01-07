from models.ID import ID


class Dish(ID):
    def __init__(self, id_: int, name: str, portionSize: int, price: int):
        super().__init__(id_)
        self.__portionSize = portionSize
        self.__price = price
        self.__name = name

    def __eq__(self, other):
        return self.__name == other.__name and self.__portionSize == other.__portionSize and self.__price == other.__price

    def __str__(self):
        return f"Name = '{self.__name}', Portionsgroesse = '{self.__portionSize}', Preis = '{self.__price}'"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def portionSize(self):
        return self.__portionSize

    @portionSize.setter
    def portionSize(self, portionSize):
        self.__portionSize = portionSize

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
