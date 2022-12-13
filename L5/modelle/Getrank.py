from modelle.Gericht import Gericht


class Getrank(Gericht):
    def __init__(self, portionsgrose: float, preis: float, alcohoolgehalt: float = 0, id_ = -1):
        id_ = hash(self) if id_ == -1 else id_

        super().__init__(portionsgrose, preis, id_)
        self.__alcohoolgehalt = alcohoolgehalt

    def __str__(self):
        return f"portionsgrosse: {self.portionsgrosse}, preis: {self.preis}, alcohoolgehalt: {self.__alcohoolgehalt}"