class Point:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def can_move(self, x, y):
        return (0 < self.x + x <= self.size) and (0 < self.y + y <= self.size)
