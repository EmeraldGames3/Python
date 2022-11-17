class statistics:
    def __init__(self, carList=None):
        if carList is None:
            carList = []
        self.carList = carList

    def numberOfSameColouredCars(self, colour):
        n = 0
        for c in self.carList:
            if colour == c.farbe:
                n += 1

        return n

    def mittlerenBaujahr(self):
        ma = 0
        for c in self.carList:
            ma += c.baujahr

        return ma / len(self.carList)
