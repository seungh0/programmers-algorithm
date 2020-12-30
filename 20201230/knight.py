import unittest

moving = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]


class Position:
    def __init__(self, x, y, max_size):
        self.max_size = max_size
        self.x = x
        self.y = y

    def is_in_range(self, n):
        return 1 <= n <= self.max_size

    def can_move(self, x, y):
        return self.is_in_range(self.x + x) and self.is_in_range(self.y + y)


def solution(pos):
    row, column = ord(pos[0]) - 96, int(pos[1])
    position = Position(row, column, 8)

    cnt = 0
    for x, y in moving:
        if position.can_move(x, y):
            cnt += 1
    return cnt


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = solution('a1')
        self.assertEqual트(result, 2)

    def test_case_2(self):
        result = solution('c2')
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
