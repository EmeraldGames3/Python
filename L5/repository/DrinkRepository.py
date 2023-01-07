from repository.Repository import Repository
from repository.formaters.DrinkFormatter import DrinkFormatter


class DrinkRepository(Repository):

    def __init__(self, path):
        super().__init__(DrinkFormatter(path))
