import hashlib


from models.Dish import Dish


class CookedDish(Dish):
    def __init__(self, id_: int, name: str, portionSize: int, price: int, prepTime: int):
        super().__init__(id_, name, portionSize, price)
        self.__prepTime = prepTime