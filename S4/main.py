import lst_functions
import utils
from Rational import Rational

lst = [Rational(1, 2), Rational(1, 3), Rational(1, 4), Rational(1, 5)]


options = {
    "a": utils.a,
    "b": utils.b,
    "c": lst_functions.sumOfList,
}


def run():
    while True:
        lst_functions.printLst(lst)
        utils.printOptions()
        option = input("Your option ").strip()

        if option in options:
            options[option](lst)
        else:
            print("Invalid option")
            break


run()
