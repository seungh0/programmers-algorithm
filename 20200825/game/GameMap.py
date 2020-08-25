class GameMap:
    def __init__(self, size, location):
        self.size_x, self.size_y = size
        self.location = location

    def convert_land_to_sea(self, x, y):
        self.location[x][y] = 1

    def is_land(self, x, y):
        if self.is_out_or_map(x, y):
            return False
        return self.location[x][y] == 0

    def is_out_or_map(self, x, y):
        return x >= self.size_x or y >= self.size_y or x < 0 or y < 0