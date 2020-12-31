import unittest

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 0(북), 1(동), 2(남), 3(서)

class Position:
    def __init__(self, x, y, direction, place):
        self.x = x
        self.y = y
        self.direction = direction
        self.place = place
        self.max_size = len(place)

    def in_map_range(self, x, y):
        return 0 <= x <= self.max_size - 1 and 0 <= y <= self.max_size - 1

    def is_land(self, x, y):
        return self.place[x][y] == 0

    def can_move(self):
        x, y = move[self.direction]
        return self.in_map_range(self.x + x, self.y + y) and self.is_land(self.x + x, self.y + y)

    def turn_left(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction = 3

    def move(self):
        self.place[self.x][self.y] = 1
        x, y = move[self.direction]
        self.x += x
        self.y += y

    def turn_back(self):
        for i in range(2):
            self.turn_left()


def solution(x, y, direction, place):
    cnt = 1
    turn_time = 0
    pos = Position(x, y, direction, place)
    while True:
        pos.turn_left()
        turn_time += 1
        if pos.can_move():
            pos.move()
            turn_time = 0
            cnt += 1

        if turn_time == 4:
            pos.turn_back()
            if pos.can_move():
                cnt += 1
                pos.move()
            else:
                break
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(1, 1, 0, [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
