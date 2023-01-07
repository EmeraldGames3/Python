class ID:
    def __init__(self, id_: int):
        self.id = id_

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_
