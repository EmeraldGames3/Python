from repository.order_repo import OrderRepo

repo = OrderRepo('repository/data')

obj_list = repo.load('orders.txt')
str_list = repo.convert_to_str(obj_list)

[print(order) for order in str_list]
