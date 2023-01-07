class ID:
    def __init__(self, id_=-1):
        self.id = id_ if id_ != -1 else hash(self)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_
