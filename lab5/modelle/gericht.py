from modelle.identifizierbar import identifizierbar


class gericht(identifizierbar):
    def __init__(self, portionsGroesse: int, preis: float):
        # Type Safety
        if type(portionsGroesse) != int or type(preis) != float:
            raise AttributeError

        super().__init__()
        self.__portionsGroesse = portionsGroesse
        self.__preis = preis

    @property
    def portionsGroesse(self):
        return self.__portionsGroesse

    @portionsGroesse.setter
    def portionsGroesse(self, x: int):
        # Type Safety
        if type(self.__portionsGroesse) != int:
            raise AttributeError

        self.__portionsGroesse = x

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, x: float):
        # Type Safety
        if type(self.__preis) != float:
            raise AttributeError

        self.__preis = x
