from models.CookedDish import CookedDish
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from ui.Menu import Menu

"""
In this folder we generate the menu and test if it was succesfull
"""

customer_repo = CustomerRepo("customers.txt")
dish_repo = CookedDishRepo("dishes.txt")
drinks_repo = DrinkRepo("drinks.txt")

dishes = [CookedDish(0, "Pizza", 450, 12, 15), CookedDish(1, "Ciorba de burta", 350, 24, 45)]
dish_repo.save(dishes)
drinks = drinks_repo.load()

menu = Menu(dishes, drinks)

def test_generate_menu():
    print(menu)

    assert "Pizza" in str(menu) and "Ciorba de burta" in str(menu) and "Vodka" in str(menu)


test_generate_menu()
