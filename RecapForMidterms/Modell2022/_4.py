class square:
    def _init_(self, x, y, side=1):
        self.x = x
        self.y = y
        self.side = side


class rectangle:
    def _init_(self, length, width, x, y):
        self.length = length
        self.width = width
        self.x = x
        self.y = y


def contains(lst: list[square], r: rectangle):
    r_x = r.x + r.length
    r_y = r.y + r.width

    for s in lst:
        s_x = s.x + s.side
        s_y = s.y + s.side

        if s.x < r.x:
            return False
        if s.y > r.y:
            return False
        if s_x > r_x:
            return False
        if s_y < r_y:
            return False

    return True