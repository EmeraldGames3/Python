class Room:
    def __init__(self, number: str, places: int):
        self.number = number
        self.places = places

    def __eq__(self, other):
        return self.number == other.number and self.places == other.places

    def __str__(self):
        return f"Number: {self.number}, Places: {self.places}"


class ComputerRoom(Room):
    os = ("Unix", "Linux", "MacOS", "Windows")

    def __init__(self, number: str, places: int, operatingSystem: str):
        if operatingSystem not in ComputerRoom.os:
            raise AttributeError("Not a valid operating system")

        super().__init__(number, places)
        self.operatingSystem = operatingSystem

    def __eq__(self, other):
        return self.number == other.number and self.places == other.places and other.operatingSystem == self.operatingSystem

    def __str__(self):
        return f"Number: {self.number}, Places: {self.places}, OS: {self.operatingSystem}"


class Building:
    def __init__(self, roomList: list):
        # for r in roomList:
        #     if type(r) != Room and type(r) != ComputerRoom:
        #         raise AttributeError("Expected a list of type Room")

        self.roomList = roomList

    def numberOfPlaces(self, roomNumber: int):
        for r in self.roomList:
            if r.number == roomNumber:
                return r.places

    def readData(self):
        with(open("data.txt") as f):
            for line in f:
                self.roomList.append(interpretFromString(line.strip("\n")))

    def writeData(self):
        f = open("data.txt", "w")

        for r in self.roomList:
            f.write(str(r) + "\n")

        f.close()


def interpretFromString(s: str):
    s = s.split(",")

    if len(s) == 2:
        s[0] = s[0].split(":")[1]
        s[1] = s[1].split(":")[1]
        return Room(s[0].strip(), int(s[1].strip()))
    elif len(s) == 3:
        s[0] = s[0].split(":")[1]
        s[1] = s[1].split(":")[1]
        s[2] = s[2].split(":")[1]
        return ComputerRoom(s[0].strip(), int(s[1].strip()), s[2].strip())


def main():
    l = [Room("12", 3), Room("123", 5), Room("121", 9), Room("1215", 7), ComputerRoom("1", 7, "Linux")]
    B = Building(l)
    # print(B.roomList)
    # print(l)

    B.writeData()
    B2 = Building([])
    B2.readData()

    for e in B2.roomList:
        print(e, end=", ")


main()
