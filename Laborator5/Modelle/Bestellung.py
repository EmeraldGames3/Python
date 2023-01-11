from datetime import datetime, timedelta
from functools import reduce

from Modelle.Identifizierbar import Identifizierbar
from Modelle.Needed_dict import menu_preis_dict_drinks, menu_preis_dict_speise, menu_dict_speise, menu_dict_drinks
from Repository.CustomerRepo import CustomerFormatter


class Order(Identifizierbar):
    """
       Order class with the following attributes:
                                                               customer id
                                                               list ids drinks
                                                               list ids dishes



    """
    def __init__(self, kunde_id, liste_id_drinks, liste_id_dish):
        self.kunde_id = kunde_id
        self.liste_id_drinks = liste_id_drinks
        self.liste_id_dish = liste_id_dish
        self.gesammtkosten = 0
        super().__init__()

    def time_stamp(self):
        """

        datetime.isoformat()=> Return a string representing the date and time in ISO 8601 format:

                                YYYY-MM-DDTHH:MM:SS.ffffff, if microsecond is not 0

                                YYYY-MM-DDTHH:MM:SS, if microsecond is 0
        :return: the exact time the order was placed

        """
        return datetime.now().isoformat()

    def compute_etd(self):
        """
        steps: 1. using the given ids, track the objects => store the objects in the list 'dishes'
            (menu_dict_speise is a dictionary, where the key is the id of an object and the value is the object itself)
            2. which dish will take the longest to be ready => max_prep_time
                - using the max function : key = dish. zubereitungszeit
            3.datetime.fromisoformat=> Return a datetime corresponding to a date_string
            4.datetime.timedelta =>A duration expressing the difference between two date, time,
            or datetime instances to microsecond resolution.

        :return: the exact time at which the order will be ready
        """
        dishes = []
        dict_dish = menu_dict_speise()
        for dish_id in self.liste_id_dish:
            dishes.append(dict_dish[dish_id])
        max_prep_time = max(dishes, key=lambda dish: dish.zubereitungszeit).zubereitungszeit
        etd = datetime.fromisoformat(self.time_stamp()) + timedelta(minutes=int(max_prep_time[:2]))
        return etd.isoformat()

    def __str__(self):
        return f"{self.id} || {self.kunde_id} || {self.liste_id_drinks} || {self.liste_id_dish}"

    def total_price(self):
        """
        steps:
                1. menu_preis_dict_drinks,menu_preis_dict_speise functions returning a dict
                (key = id,value = price )
                2. create a list of prices: price_list
                3. calculate total sum using reduce funtion(imported from functools)
        :return: the total price of the order
        """
        drink_price_dict = menu_preis_dict_drinks()
        dish_price_dict = menu_preis_dict_speise()
        price_list = []
        for id_dish in self.liste_id_dish:
            price_list.append(int(dish_price_dict[id_dish]))
        for id_drink in self.liste_id_drinks:
            price_list.append(int(drink_price_dict[id_drink]))

        self.gesammtkosten = reduce(lambda x, y: x + y, price_list)
        return self.gesammtkosten

    def generate_bill(self):
        """
        
        :return: bill lines
        """
        dish_dict = menu_dict_speise()
        drink_dict = menu_dict_drinks()
        items = list(map(lambda dish_id: dish_dict[dish_id], self.liste_id_dish))

        for drink_id in self.liste_id_drinks:
            items.append(drink_dict[drink_id])
        bill_lines = list(map(lambda item: f"{item.name} " + "." * (30 - len(item.name)) + f" {item.preis}", items))
        bill_lines.append(f"Total price " + '.' * 19 + f" {self.total_price()}")
        time = datetime.fromisoformat(self.time_stamp()).strftime(" %R ")
        etd = datetime.fromisoformat(self.compute_etd()).strftime(" %R ")
        bill_lines.append(f"Received order at: {time}")
        bill_lines.append(f"Order will be ready at: {etd}")
        return bill_lines

    def print_bill(self):
        print()
        print()
        print("                                                                                 RECHNUNG     ")
        print()
        print()
        bill_lines = self.generate_bill()
        for bill_line in bill_lines:
            print("                                                                  ",bill_line)

    def print_bill_and_customer_info(self):
        customer_formatter = CustomerFormatter('../Files/Customer_Database')
        customer_liste = customer_formatter.load()
        bill_lines = self.generate_bill()
        for customer in customer_liste:
            if int(self.kunde_id) == int(customer.id):
                bill_lines.append(f"Customers name: {customer.name}")
                bill_lines.append(f"Customers address: {customer.adresse}")
        for bill_line in bill_lines:
            print(bill_line)

