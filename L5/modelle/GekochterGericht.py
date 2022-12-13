from modelle.Gericht import Gericht


class GekochterGericht(Gericht):
    def __init__(self, portionsGrosse: float, preis: float, zubereitungZeit: float, id_=-1):
        id_ = hash(self) if id_ == -1 else id_

        super().__init__(portionsGrosse, preis, id_)
        self.zubereitungZeit = zubereitungZeit

    def __str__(self):
        return f"portions grosse: {self.portionsgrosse}, preis: {self.preis}, zubereitung Zeit: {self.zubereitungZeit},"


g = GekochterGericht(1, 1, 1)
print(g.id)
