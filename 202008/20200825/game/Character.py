MOVE = [
    [-1, 0],  # NORTH
    [0, 1],  # EAST
    [1, 0],  # SOUTH
    [0, -1]  # WEST
]


class Character:
    def __init__(self, x, y, direction, game_map):
        self.x = x
        self.y = y
        self.direction = direction  # (0, 북), (1, 동), (2, 남), (3, 서)
        self.game_map = game_map

    def turn_left(self):
        self.direction -= 1
        if self.direction == -1:
            self.direction = 3

    def can_move_forward(self):
        x = self.x + MOVE[self.direction][0]
        y = self.y + MOVE[self.direction][1]
        return self.game_map.is_land(x, y)

    def move_forward(self):
        self.x += MOVE[self.direction][0]
        self.y += MOVE[self.direction][1]
        self.check_in(self.x, self.y)

    def can_move_back(self):
        x = self.x - MOVE[self.direction][0]
        y = self.y - MOVE[self.direction][1]
        return self.game_map.is_land(x, y)

    def move_back(self):
        self.x -= MOVE[self.direction][0]
        self.y -= MOVE[self.direction][1]
        self.check_in(self.x, self.y)

    def check_in(self, x, y):
        self.game_map.convert_land_to_sea(x, y)
