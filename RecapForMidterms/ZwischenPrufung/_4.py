"""
Eine solche datenstruktur kann man als eine Liste von Listen von listen implementieren oder
man kann eine class bauen die einen Solchem objekt erzeugt
"""


class UselessMatrix:
    def __init__(self, lines):
        self.lines = lines

    def add_line(self, line: list[list[int]]):
        self.lines.append(line)

    def sort_line(self, index: int):
        self.lines[index].sort(key=lambda x: x[1])

    def __sub__(self, other):
        result = []
        for i in range(len(self.lines)):
            line = []
            for j in range(len(self.lines[i])):
                useless_element = []
                for k in self.lines[i][j]:
                    if k not in other.lines[i][j]:
                        useless_element.append(k)
                line.append(useless_element)
            result.append(line)
        return UselessMatrix(result)

    def __str__(self):
        s = "[\n"

        for l in self.lines:
            s += (str(l) + "\n")

        s += "]"
        return s


m = UselessMatrix(
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 3]],
        [[8, 9], [9, 10]]
    ]
)

m6 = UselessMatrix(
    [
        [[1], [3, 4]],
        [[5], [7, 3]],
        [[8], [9, 10]]
    ]
)

print(m)
print(m - m)
print(m - m6)
print(m6)

m.sort_line(1)
print(m)
