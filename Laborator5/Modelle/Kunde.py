from Modelle.Identifizierbar import Identifizierbar


class Customer(Identifizierbar):
    def __init__(self, name=None, adresse=None):
        self.name = name
        self.adresse = adresse
        super().__init__()

    def __str__(self):
        return f"{self.id},{self.name},{self.adresse}"
