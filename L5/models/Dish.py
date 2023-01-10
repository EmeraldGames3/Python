from models.ID import ID


class Dish(ID):
    def __init__(self, id_: int, name: str, portionSize: int, price: int):
        super().__init__(id_)
        self.__portionSize = portionSize
        self.__price = price
        self.__name = name