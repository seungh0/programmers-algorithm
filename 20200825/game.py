import unittest

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


class Character:
    def __init__(self, x, y, direction, my_map, size):
        self.x = x
        self.y = y
        self.direction = direction  # (0, 북), (1, 동), (2, 남), (3, 서)
        self.my_map = my_map
        self.size_x = size[0]
        self.size_y = size[1]

    def turn_left(self):
        self.direction -= 1
        if self.direction == -1:
            self.direction = 3

    def can_move(self):
        x = self.x + dx[self.direction]
        y = self.y + dy[self.direction]
        if x >= self.size_x or y >= self.size_y or x < 0 or y < 0:
            return False
        return self.my_map[x][y] == 0

    def move(self):
        self.x += dx[self.direction]
        self.y += dy[self.direction]
        self.my_map[self.x][self.y] = 1

    def can_move_back(self):
        x = self.x - dx[self.direction]
        y = self.y - dy[self.direction]
        if x >= self.size_x or y >= self.size_y or x < 0 or y < 0:
            return False
        return self.my_map[x][y] == 0

    def move_back(self):
        self.x -= dx[self.direction]
        self.y -= dy[self.direction]
        self.my_map[self.x][self.y] = 1


def solution(size, start, location):
    character = Character(start[0], start[1], start[2], location, size)

    cnt = 1
    turn_time = 0
    character.my_map[start[0]][start[1]] = 1
    while True:
        character.turn_left()
        if character.can_move():
            character.move()
            cnt += 1
            turn_time = 0
        else:
            turn_time += 1

        if turn_time == 4:
            # 뒤로 갈 수 있으면? 가고 아니면 return ctn
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
