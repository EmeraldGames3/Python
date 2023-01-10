from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo
from ui.RestaurantMenu import RestaurantMenu
from ui.UserMenu import print_starting_menu


def main_menu(customerRepo: CustomerRepo, cookedDishRepo: CookedDishRepo, drinkRepo: DrinkRepo, orderRepo: OrderRepo):
    while True:
        customers = customerRepo.load()
        dishes = cookedDishRepo.load()
        drinks = drinkRepo.load()
        orders = orderRepo.load()

        restaurant_menu = RestaurantMenu(dishes, drinks)

        print_starting_menu()

        option = int(input("Your option: "))

        if option == 1:
            print(restaurant_menu)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            pass
        elif option == 10:
            pass
        elif option == 11:
            pass
        elif option == 12:
            return
        else:
            pass

        customerRepo.save(customers)
        cookedDishRepo.save(dishes)
        drinkRepo.save(drinks)
        orderRepo.save(orders)