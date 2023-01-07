from repository.Repository import Repository
from repository.formaters.OrderFormatter import OrderFormatter


class OrderRepository(Repository):

    def __init__(self, path):
        super().__init__(OrderFormatter(path))
