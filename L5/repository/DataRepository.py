class DataRepo:
    def __init__(self, datei: str):
        self.datei = datei

    def save(self, l):
        s = self.convertToString()
        self.writeToFile(s)

    def load(self):
        s = self.readFile()
        return self.convertFromString(s)

    def readFile(self):
        with(open(self.datei) as f):
            return f.read()

    def writeToFile(self, s: str):
        f = open(self.datei, "w")
        f.write(s)
        f.close()

    def convertToString(self):
        pass

    def convertFromString(self):
        pass
