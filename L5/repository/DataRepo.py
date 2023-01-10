class DataRepo:
    def __init__(self, file):
        self.file = file

    def add(self, obj):
        objList = self.load()
        objList.append(obj)
        self.save(objList)

    def save(self, objList):
        self.writeToFile(self.convertToString(objList))

    def load(self):
        return self.convertFromString(self.readFile())

    def readFile(self):
        with open(self.file, 'r') as f:
            content = f.read()
            f.close()
        return content

    def writeToFile(self, content):
        with open(self.file, 'w') as f:
            f.write(content)

    def convertToString(self, obj_list):
        pass

    def convertFromString(self, string):
        pass