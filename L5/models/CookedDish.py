from models.Dish import Dish


class CookedDish(Dish):
    def __init__(self, id_: int, name: str = "Fisch und Chips", portionSize: int = 420, price: int = 69, prepTime: int = 100):
        super().__init__(id_, name, portionSize, price)
        self.prepTime = prepTime

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, portions Groesse: {self.portionSize}, Zubereitungszeit: {self.prepTime}, Preis: {self.price}"
