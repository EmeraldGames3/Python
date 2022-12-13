from modelle.identifizierbar import Identifizierbar


class Gericht(Identifizierbar):
    def __init__(self, portionsgrose: float, preis: float, id_):
        super().__init__(id_)
        self.__portionsgrose = portionsgrose
        self.__preis = preis

    @property
    def portionsgrosse(self):
        return self.__portionsgrose

    @portionsgrosse.setter
    def portionsgrosse(self, x):
        self.__preis = x

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, x):
        self.__preis = x
