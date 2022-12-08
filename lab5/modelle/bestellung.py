from modelle.identifizierbar import Identifizierbar


class Bestellung(Identifizierbar):
    def __init__(self, kundenID: int, bestellungListe: list, gesamtkosten: float):
        # Type Safety
        if type(kundenID) != int or type(bestellungListe) != list or type(gesamtkosten) != float:
            raise AttributeError

        super().__init__()
        self.__gesamtkosten = gesamtkosten
        self.__bestellungListe = bestellungListe
        self.__kundenID = kundenID

    @property
    def gesamtkosten(self):
        return self.__gesamtkosten

    @gesamtkosten.setter
    def gesamtkosten(self, x: float):
        # Type Safety
        if type(self.__gesamtkosten) != float:
            raise AttributeError

        self.__gesamtkosten = x

    @property
    def bestellungListe(self):
        return self.__bestellungListe

    @bestellungListe.setter
    def bestellungListe(self, x: int):
        # Type Safety
        if type(self.__kundenID) != int:
            raise AttributeError

        self.__bestellungListe = x

    @property
    def kundenID(self):
        return self.__kundenID

    @kundenID.setter
    def kundenID(self, x: list):
        # Type Safety
        if type(self.__bestellungListe) != list:
            raise AttributeError

        self.__kundenID = x
