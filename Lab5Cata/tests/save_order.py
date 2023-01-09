from controller.controller import Controller
from repository.order_repo import OrderRepo

controller = Controller(OrderRepo('repository/data'))
controller.generate_order(id='10', client_id='5', drinks_list=['1', '0'], cooked_dishes_list=['1', '1'],
                          time_placed='10:12', expected_time='11:12')
