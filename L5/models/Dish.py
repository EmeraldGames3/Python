from models.ID import ID


class Dish(ID):
    def __init__(self, id_: int, name: str, portionSize: int, price: int):
        super().__init__(id_)
        self.portionSize = portionSize
        self.price = price
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, portion Size: {self.portionSize}g, price: {self.price}$"
