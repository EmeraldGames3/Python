class DataFormatter:
    def __init__(self, file):
        self.__file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file = file

    def save(self, obj_list):
        """
        Converts a list of objects to a pickle string and writes it to self.__file
        :param obj_list:
        """
        self.writeToFile(self.convertToString(obj_list))

    def load(self):
        """
        Reads the pickle string from self.__file and converts it to a list of objects
        :returns: A list of objects | -1 if file is empty
        :rtype: list[Identifiable] | int
        """
        contents = self.readFile()
        if contents == "":
            return -1

        return self.convertFromString(contents)

    def readFile(self):
        """
        Reads and returns the contents of self.__file
        :rtype: str
        """
        with open(self.__file, 'rb') as f:
            content = f.read()
            f.close()

        return content

    def writeToFile(self, content):
        """
        Writes content to self.__file
        :param content:
        """
        with open(self.__file, 'wb') as f:
            f.write(content)
            f.close()

    def clearFile(self):
        """
        Clears self.__file
        """
        open(self.__file, 'wb').close()

    def convertToString(self, obj_list):
        """
        Abstract method to be implemented in subclasses of DataFormatter.
        Converts a list of objects to a pickle string
        :param obj_list:
        :rtype: str
        """
        pass

    def convertFromString(self, string):
        """
        Abstract method to be implemented in subclasses of DataFormatter.
        Converts a pickle string to a list of objects
        :param string:
        :rtype: list
        """
        pass
