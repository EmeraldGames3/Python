from models.CookedDish import CookedDish
from repository.CookedDishRepo import CookedDishRepo


def add_dish_test():
    repo = CookedDishRepo("dishes.txt")
    dish1 = CookedDish(0, "Pizza de cartofi", 450, 12, 15)
    dish2 = CookedDish(0, "Pizza de telemea", 450, 12, 15)
    repo.save([dish1])

    readDish1 = repo.load()[0]
    readDish2 = repo.load()[1]
    assert dish1 == readDish1
    assert dish2 == readDish2


add_dish_test()
