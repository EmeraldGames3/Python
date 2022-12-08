from modelle.identifizierbar import Identifizierbar


class Kunde(Identifizierbar):
    def __init__(self, name: str, adresse: str):
        # Type Safety
        if type(name) != str or type(adresse) != str:
            raise AttributeError

        super().__init__()
        self.__adresse = adresse
        self.__name = name

    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresse(self, x: str):
        # Type Safety
        if type(self.__adresse) != float:
            raise AttributeError

        self.__adresse = x

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x: str):
        # Type Safety
        if type(self.__name) != float:
            raise AttributeError

        self.__name = x
