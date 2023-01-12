def concatenate_strings_random(t):
    l = []

    for e1 in t:
        for e2 in t:
            if e1 != e2:
                l += [e1 + e2]

    return tuple(list(t) + l)


# print(concatenate_strings_random(("rot", "blau", "grun")))

temp_c = ("rot", "blau", "grun")


class Cartridge:
    __color = concatenate_strings_random(temp_c)

    def __init__(self, tintestand: int, farbe: str):
        if tintestand < 0:
            raise AttributeError("Ink content cannot be lower than 0")

        self.tintestand = tintestand

        if farbe not in Cartridge.__color:
            raise AttributeError("not a valid color")

        self.farbe = farbe

    def __add__(self, other):
        if isinstance(other, Cartridge):
            new_ink_level = self.tintestand + other.tintestand

            new_ink_level = 100 if new_ink_level > 100 else new_ink_level

            new_color = self.farbe + other.farbe
            return Cartridge(new_ink_level, new_color)
        else:
            raise TypeError

    def __str__(self):
        return f"ink content: {self.tintestand}, ink color: {self.farbe}"

    def __repr__(self):
        return f"ink content: {self.tintestand}, ink color: {self.farbe}"


class Printer:
    def __init__(self):
        self.cartridges = []

    def add_cartridge(self, cartridge: Cartridge):
        if cartridge.tintestand == 0:
            raise RuntimeError("Cannot add empty Cartridge")

        if len(self.cartridges) > 2:
            raise RuntimeError("Printer can only have three cartridges")

        for c in self.cartridges:
            if c.farbe == cartridge.farbe and c.tintestand > 0:
                raise RuntimeError("You can only replace empty cartridges")

        self.cartridges.append(cartridge)

    def remove_cartridge(self, color):
        for cartridge in self.cartridges:
            if cartridge.farbe == color:
                self.cartridges.remove(cartridge)
                return

        raise RuntimeError("No cartridge found")

    def print(self, l: list[str], file: str = "Printer.txt"):
        f = open(file, "w")

        for line in l:
            f.write(line + "\n")

        f.close()


class SmartPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print(self, l: list[str], file: str = "Printer.txt"):
        super().print(l, file)

        n = len("".join(l))

        print(f"Printed a document of length {n} to path {file}")


def check():
    cartridge1 = Cartridge(50, 'rot')
    cartridge2 = Cartridge(70, 'blau')

    cartridge3 = cartridge1 + cartridge2

    print(cartridge1)
    print(cartridge2)
    print(cartridge3)

    assert isinstance(cartridge3, Cartridge)
    assert cartridge3 is not cartridge1
    assert cartridge3.farbe == 'rotblau'
    assert cartridge3.tintestand == 100


check()
sm = SmartPrinter()
sm.print(["Ana", "are", "mere"])
sm.add_cartridge(Cartridge(50, "rot"))
sm.cartridges[0].tintestand = 0

sm.remove_cartridge("rot")

cartridge1 = Cartridge(50, 'rot')
cartridge2 = Cartridge(70, 'blau')

cartridge3 = cartridge1 + cartridge2

sm.add_cartridge(cartridge1)
sm.add_cartridge(cartridge2)
sm.add_cartridge(cartridge3)

print(sm.cartridges)
