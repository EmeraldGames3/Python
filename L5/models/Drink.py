from models.Dish import Dish


class Drink(Dish):
    def __init__(self, portionsgrose: float, preis: float, alcohoolgehalt: float = 0, id_=-1):
        super().__init__(portionsgrose, preis, id_)
        self.__alcohoolgehalt = alcohoolgehalt
