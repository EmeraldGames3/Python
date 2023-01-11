from Modelle.Gericht import Gericht


class Gekochter_Gericht(Gericht):
    """
    Gekochter_Gericht class with the following attributes:
                                                           name
                                                           preis(inherited from the super class Gericht)
                                                           zubereitungszeit
                                                           portionsgrosse(inherited from the super class Gericht)


    """
    def __init__(self, name=None, zubereitungszeit=None, portionsgrosse=None, preis=None):
        self.zubereitungszeit = zubereitungszeit
        self.name = name
        super().__init__(portionsgrosse, preis)

    def __str__(self):
        return f"{self.id},{self.name},{self.zubereitungszeit},{self.portionsgrosse},{self.preis}"
