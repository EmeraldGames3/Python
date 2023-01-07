import hashlib

from models.Dish import Dish


class CookedDish(Dish):
    def __init__(self, id_: int, name: str, portionSize: int, price: int, prepTime: int):
        super().__init__(id_, name, portionSize, price)
        self.__prepTime = prepTime

    def __eq__(self, other):
        return super().__eq__(other) and self.__prepTime == other.__prep_time

    def __str__(self):
        return super().__str__() + f", Zubereitungszeit = '{self.__prepTime}'"

    def __hash__(self):
        encodedString = self.__str__().encode()
        return hashlib.sha1(encodedString).hexdigest()

    @property
    def prepTime(self):
        return self.__prepTime

    @prepTime.setter
    def prepTime(self, prepTime):
        self.__prepTime = prepTime
