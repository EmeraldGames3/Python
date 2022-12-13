from modelle.identifizierbar import Identifizierbar


class Kunde(Identifizierbar):
    def __init__(self, name: str, adresse: str):
        super().__init__(hash(str(self)))
        self.name = name
        self.adresse = adresse

    def __str__(self):
        return f"Name: {self.name}, Adresse: {self.adresse}"