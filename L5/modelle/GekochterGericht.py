from modelle.Gericht import Gericht


class GekochterGericht(Gericht):
    def __init__(self, portionsGrosse: float, preis: float, zubereitungZeit: float, id_=-1):
        super().__init__(portionsGrosse, preis, id_)
        self.zubereitungZeit = zubereitungZeit
