from models.Dish import Dish


class Drink(Dish):
    def __init__(self, id_: int, name: str = "Vodka", portionSize: int = 100, price: int = 50,
                 alcoholContent: int = 95):
        super().__init__(id_, name, portionSize, price)
        self.alcoholContent = alcoholContent

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, portions Groesse: {self.portionSize}ml, Alkohoolgehalt: {self.alcoholContent}%, Preis: {self.price}$"
