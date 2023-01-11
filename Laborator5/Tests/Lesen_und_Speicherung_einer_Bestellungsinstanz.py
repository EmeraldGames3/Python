from Controller.Order import *


def main():

    order_formatter = OrderFormatter('../Files/Order_Database')
    order_list = order_formatter.load()
    print(order_list[0].kunde_id)
    order=Order(110867797491,[139178093460],[139178093460])
    order_list.append(order)
    order_formatter.save(order_list)
    show_orders()
main()
