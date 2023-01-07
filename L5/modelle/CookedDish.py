from modelle.Dish import Dish


class GekochterGericht(Dish):
    def __init__(self, portionsGrosse: float, preis: float, zubereitungZeit: float, id_=-1):
        super().__init__(portionsGrosse, preis, id_)
        self.zubereitungZeit = zubereitungZeit
