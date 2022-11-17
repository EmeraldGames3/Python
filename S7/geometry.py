from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class circle:
    def __init__(self, radius, center=Point(0, 0)):
        self.radius = radius
        self.center = center

    def makeItBig(self, num):
        # Small
        self.radius += num


class triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

        self.ab = sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
        self.ac = sqrt((a.x - c.x) ** 2 + (a.y - c.y) ** 2)
        self.bc = sqrt((c.x - b.x) ** 2 + (c.y - b.y) ** 2)

    def makeItBig(self, num):
        # Small
        self.a += num
        self.b += num
        self.c += num

    def rotate(self, num):
        if num % 3 == 1:
            self.a = self.c
            self.b = self.a
            self.c = self.b
        elif num % 3 == 2:
            self.a = self.b
            self.b = self.c
            self.c = self.a
        elif num % 3 == 0:
            return
