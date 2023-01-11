from Controller.Order import *
def rechnung_darstellung_testen():

    order_formatter = OrderFormatter('../Files/Order_Database')
    order_list = order_formatter.load()
    order=order_list[0]
    order.print_bill()

rechnung_darstellung_testen()