class DataFormatter:
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, list):
        self.write_to_file(self.convert_to_string(list))

    def load(self):
        contents = self.read_file()
        if contents == "":
            return -1

        return self.convert_from_string(contents)

    def read_file(self):
        file = open(self.file_name, 'r')
        content = file.read()
        file.close()
        return content

    def write_to_file(self, string):
        file = open(self.file_name, 'w')
        file.write(string)
        file.close()

    def convert_to_string(self, liste):
        pass

    def convert_from_string(self, string):
        pass
