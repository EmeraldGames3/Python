from modelle.order import Order

order = Order(id='10', client_id='5', drinks_list=['1', '0'], cooked_dishes_list=['1', '1'], time_placed='10:12',
              expected_time='11:12')
order.print_check()
