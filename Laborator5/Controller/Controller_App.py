from Controller.Menu import *
from Controller.Order import *
from UI.For_controller import *


def controller():
    print_on_screen_controller()
    option = for_option()
    complete = False
    while not complete:
        match option:
            case 1:
                menu_controller()
                answere = return_to_menu()
                match answere:
                    case 'yes':
                        controller()
                    case 'no':
                        complete = True

            case 2:
                customer_controller()
                answere = return_to_menu()
                match answere:
                    case 'yes':
                        controller()
                    case 'no':
                        complete = True

            case 3:
                order_controller()
                answere = return_to_menu()
                match answere:
                    case 'yes':
                        controller()
                    case 'no':
                        complete = True

            case 4:
                complete = True

    print("Changes were made succesfully")

