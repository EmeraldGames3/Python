from modelle.ID import ID


class Customer(ID):
    def __init__(self, name: str, adresse: str, id_=-1):
        super().__init__(id_)
        self.name = name
        self.adresse = adresse
