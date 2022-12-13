class Identifizierbar:
    def __init__(self, id_):
        self.__id = id_

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, x):
        self.__id = x