from repository.Repository import Repository
from repository.formaters.CustomerFormatter import CustomerFormatter


class CustomerRepository(Repository):

    def __init__(self, path):
        super().__init__(CustomerFormatter(path))
