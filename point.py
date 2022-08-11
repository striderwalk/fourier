from typing import NamedTuple


class Point(NamedTuple):
    """
    a simplified vector
    """

    x: int
    y: int

    def __mul__(self, num):
        if isinstance(num, int):
            return Point(self.x * num, self.y * num)
        elif isinstance(num, float):
            return Point(self.x * num, self.y * num)
        elif isinstance(num, Point):
            return Point(self.x * num.x, self.y * num.y)
        elif isinstance(num, tuple):
            return Point(self.x * num[0], self.y * num[1])
        else:
            return NotImplemented

    def __truediv__(self, num):
        if isinstance(num, int):
            return Point(self.x / num, self.y / num)
        elif isinstance(num, float):
            return Point(self.x / num, self.y / num)
        elif isinstance(num, Point):
            return Point(self.x / num.x, self.y / num.y)
        elif isinstance(num, tuple):
            return Point(self.x / num[0], self.y / num[1])
        else:
            return NotImplemented

    def __add__(self, num):
        if isinstance(num, int):
            return Point(self.x + num, self.y + num)
        elif isinstance(num, float):
            return Point(self.x + num, self.y + num)
        elif isinstance(num, Point):
            return Point(self.x + num.x, self.y + num.y)
        elif isinstance(num, tuple):
            return Point(self.x + num[0], self.y + num[1])
        else:
            return NotImplemented

    def __sub__(self, num):
        if isinstance(num, int):
            return Point(self.x - num, self.y - num)
        elif isinstance(num, float):
            return Point(self.x - num, self.y - num)
        elif isinstance(num, Point):
            return Point(self.x - num.x, self.y - num.y)
        elif isinstance(num, tuple):
            return Point(self.x - num[0], self.y + num[1])
        else:
            return NotImplemented
