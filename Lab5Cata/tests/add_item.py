from controller.controller import Controller
from repository.drink_repo import DrinkRepo
from repository.cooked_dish_repo import CookedDishRepo

# adauga o bautura
controller = Controller(DrinkRepo('repository/data'))
controller.add_drink(id='10', name='Test', portion_size='123', price='15', alcohol_content='50')

# adauga un tip de mancare
controller = Controller(CookedDishRepo('repository/data'))
controller.add_cooked_dish(id='10', name='Test', portion_size='150', price='50', prep_time='30')
