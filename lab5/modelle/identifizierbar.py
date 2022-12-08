class Identifizierbar:
    __id = 1

    def __init__(self):
        self.__id = Identifizierbar.__id
        Identifizierbar.__id += 1

    @property
    def id(self):
        return self.__id
