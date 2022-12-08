from modelle.gericht import Gericht


class gekochterGericht(Gericht):
    def __init__(self, portionsGroesse: int, preis: float, zubereitungsZeit: float):
        # Type Safety
        if type(zubereitungsZeit) != float:
            raise AttributeError

        super().__init__(portionsGroesse, preis)
        self.__zubereitungsZeit = zubereitungsZeit

    @property
    def zubereitungsZeit(self):
        return self.__zubereitungsZeit

    @zubereitungsZeit.setter
    def zubereitungsZeit(self, x: float):
        # Type Safety
        if type(self.__zubereitungsZeit) != float:
            raise AttributeError

        self.__zubereitungsZeit = x
