class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Pig(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age
