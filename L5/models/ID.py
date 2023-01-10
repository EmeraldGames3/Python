class ID:
    ID = 1
    def __init__(self, id_: int):
        self.id = id_

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_

    def __str__(self):
        return f"ID: {str(self.__id)}"