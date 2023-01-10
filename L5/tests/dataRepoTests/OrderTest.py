from models.CookedDish import CookedDish
from models.Customer import Customer
from models.Order import Order
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo

customer_repo = CustomerRepo("customers.txt")
dish_repo = CookedDishRepo("dishes.txt")
drinks_repo = DrinkRepo("drinks.txt")

customer = Customer(0, "Mihai", "Str. Ciorilor")
customer_repo.save([customer])

dishes = [CookedDish(0, "Pizza", 450, 12, 15), CookedDish(1, "Ciorba de burta", 350, 24, 45)]
dish_repo.save(dishes)
drinks = drinks_repo.load()

order = Order(0, customer.id, [dishes[0].id, dishes[1].id], [drinks[0].id])
print(order)


def order_bill_test():
    bill = order.generate_bill(dishes, drinks)
    print(f"Bill: \n{bill}")
    assert "Pizza" in bill and "Ciorba de burta" in bill and "156" in bill and "Vodka" in bill


def save_load_order_test():
    order_repo = OrderRepo("orders.txt")
    order_repo.save([order])

    print(order_repo.load()[0])
    read_order = order_repo.load()[0]

    assert read_order == order


order_bill_test()
save_load_order_test()
