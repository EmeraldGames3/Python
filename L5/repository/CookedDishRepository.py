from repository.Repository import Repository
from repository.formaters.CookedDishFormatter import CookedDishFormatter


class CookedDishRepository(Repository):

    def __init__(self, path):
        super().__init__(CookedDishFormatter(path))
