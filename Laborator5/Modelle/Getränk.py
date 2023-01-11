from Modelle.Gericht import Gericht


class Getrank(Gericht):
    """
        Getrank class with the following attributes:
                                                               name
                                                               preis(inherited from the super class Gericht)
                                                               alkoholgehalt
                                                               portionsgrosse(inherited from the super class Gericht)
                                                               __str__ method (used in convert to/from string )


    """
    def __init__(self, name=None, alkoholgehalt=None, portionsgrosse=None, preis=None):
        self.alkoholgehalt = alkoholgehalt
        self.name = name
        super().__init__(portionsgrosse, preis)

    def __str__(self):
        return f"{self.id},{self.name},{self.alkoholgehalt},{self.portionsgrosse},{self.preis}"
