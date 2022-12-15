from functools import reduce

from modelle.identifizierbar import Identifizierbar


class Bestellung(Identifizierbar):
    def __init__(self, Kunden_Id: str, id_=-1):
        super().__init__(id_)
        self.Kunden_Id = Kunden_Id
        self.lst = []

    def kostenBerechnung(self):
        return reduce(lambda x, y: x + y, self.lst)
