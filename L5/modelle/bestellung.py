from functools import reduce

from modelle.identifizierbar import Identifizierbar


class Bestellung(Identifizierbar):
    def __init__(self, Kunden_Id: str):
        super().__init__(hash(self))
        self.Kunden_Id = Kunden_Id
        self.lst = []

    def kostenBerechnung(self):
        return reduce(lambda x, y: x + y, self.lst)

    def __str__(self):
        return f"Kunden Id: {self.Kunden_Id}"
