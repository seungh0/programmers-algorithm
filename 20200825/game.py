import unittest

MOVE = [
    [-1, 0],  # NORTH
    [0, 1],  # EAST
    [1, 0],  # SOUTH
    [0, -1]  # WEST
]


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


def solution(size, start, location):
    start_character_x, start_character_y, start_character_direction = start

    game_map = GameMap(size, location)
    character = Character(start_character_x, start_character_x, start_character_direction, game_map)

    cnt = 1
    turn_time = 0
    character.check_in(start_character_x, start_character_y)

    while True:
        character.turn_left()
        if character.can_move_forward():
            character.move_forward()
            cnt += 1
            turn_time = 0
        else:
            turn_time += 1

        if turn_time == 4:
            if character.can_move_back():
                character.move_back()
            else:
                break
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # given
        size = [4, 4]
        start = [1, 1, 0]
        location = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 3)

    def test_something_2(self):
        # given
        size = [3, 3]
        start = [1, 1, 0]
        location = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 2)

    def test_something_3(self):
        # given
        size = [2, 2]
        start = [1, 1, 0]
        location = [
            [0, 0],
            [0, 0],
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 4)

    def test_something_4(self):
        # given
        size = [3, 4]
        start = [1, 1, 0]
        location = [
            [1, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 0]
        ]

        # when
        result = solution(size, start, location)

        # then
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
