from controller.CustomerController import CustomerController
from controller.MenuController import MenuController
from controller.OrderController import OrderController
from repository.CookedDishRepository import CookedDishRepository
from repository.CustomerRepository import CustomerRepository
from repository.DrinkRepository import DrinkRepository
from repository.OrderRepository import OrderRepository
from ui.UIController import menu, invalid


class Controller:
    def __init__(self, db_root="repository/database/"):
        self.__customer_repo = CustomerRepository(f"{db_root}customers/customers.pickle")
        self.__order_repo = OrderRepository(f"{db_root}orders/orders.pickle")
        self.__cooked_dish_repo = CookedDishRepository(f"{db_root}menu/cooked_dishes.pickle")
        self.__drink_repo = DrinkRepository(f"{db_root}menu/drinks.pickle")

        self.customer_controller = CustomerController(self.__customer_repo)
        self.menu_controller = MenuController(self.__drink_repo, self.__cooked_dish_repo)
        self.order_controller = OrderController(self.__customer_repo, self.__order_repo, self.__cooked_dish_repo,
                                                self.__drink_repo)

    def main_menu(self):
        """
        The main menu of the application
        """
        opt = menu("Restaurant Verwaltung app", ["Bestellungen", "Speisekarte", "Kunden", "<-Exit"])
        if not opt.isnumeric():
            invalid()
            self.main_menu()

        opt = int(opt)

        if opt == 1:
            self.order_controller.menu()
            self.main_menu()
        elif opt == 2:
            self.menu_controller.menu()
            self.main_menu()
        elif opt == 3:
            self.customer_controller.menu()
            self.main_menu()
        elif opt == 4:
            # Exit program
            pass
        else:
            invalid()
            self.main_menu()
