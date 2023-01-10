from functools import reduce

from models.Customer import Customer
from repository.DataRepo import DataRepo


class CustomerRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convertToString(self, objList):
        strList = list(map(lambda item: f"{item.id},{item.name},{item.address}", objList))
        return reduce(lambda s1, s2: s1 + '\n' + s2, strList)

    def convertFromString(self, string):

        if string == "":
            return []

        def lineToDash(line):
            params = line.split(',')
            id_ = 0 if params[0] == '' else int(params[0])
            return Customer(id_, params[1], params[2])

        lines = string.split('\n')
        return list(map(lambda line: lineToDash(line), lines))

    def search(self, name=None, address=None):
        customers = self.load()
        result = None
        if name is not None:
            result = list(filter(lambda customer: name.lower() in customer.name.lower(), customers))

        if address is not None:
            result = list(filter(lambda customer: address.lower() in customer.address.lower(), customers))

        return result

    def update(self, customer, name=None, address=None):
        customers = self.load()
        index = customers.index(customer)
        if name is not None:
            customer.name = name
        if address is not None:
            customer.address = address
        customers[index] = customer

        self.save(customers)
