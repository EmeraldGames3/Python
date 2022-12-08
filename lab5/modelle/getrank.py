from modelle.gericht import Gericht


class Getrank(Gericht):
    def __init__(self, portionsGroesse: int, preis: float, alkohoolgehalt: float):
        # Type Safety
        if type(alkohoolgehalt) != float:
            raise AttributeError

        super().__init__(portionsGroesse, preis)
        self.__alkohoolgehalt = alkohoolgehalt

    @property
    def alkohoolgehalt(self):
        return self.__alkohoolgehalt

    @alkohoolgehalt.setter
    def alkohoolgehalt(self, x):
        # Type Safety
        if type(self.__alkohoolgehalt) != float:
            raise AttributeError

        self.__alkohoolgehalt = x
