from models.ID import ID


class Customer(ID):
    def __init__(self, id_: int, name: str = "Bob", address: str = "Sibiu strada Noua"):
        super().__init__(id_)
        self.name = name
        self.address = address

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Addresse: {self.address}"
