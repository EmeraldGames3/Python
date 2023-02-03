class Car:
    def __init__(self, brand: str, model: str, color: str, construction_year: int):
        self.construction_year = construction_year
        self.color = color
        self.model = model
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.model} {self.color} {self.construction_year}"

    def __repr__(self):
        return f"{self.brand} {self.model} {self.color} {self.construction_year}"


class Statistics:
    @staticmethod
    def number_of_same_colored_cars(list_of_cars: list[Car], color: str):
        return len([car for car in list_of_cars if car.color == color])


lc = [Car("Brand1", "Model1", "Red", 2000), Car("Brand2", "Model2", "Red", 2010),
      Car("Brand3", "Model3", "Green", 2005)]
number_of_red_cars = Statistics.number_of_same_colored_cars(lc, "Red")
print(number_of_red_cars)
