import unittest


class Point:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def can_move(self, x, y):
        return (0 < self.x + x <= self.size) and (0 < self.y + y <= self.size)


def solution(pos):
    x = int(ord(pos[0])) - int(ord('a')) + 1
    y = int(pos[1])
    point = Point(x, y, 8)

    steps = [
        (-2, -1), (-2, 1), (-1, 2), (-1, -2),
        (1, 2), (1, -2), (2, 1), (2, -1)
    ]

    cnt = 0
    for step in steps:
        if point.can_move(step[0], step[1]):
            cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution('a1')
        self.assertEqual(result, 2)

    def test_something_2(self):
        result = solution('h8')
        self.assertEqual(result, 2)

    def test_something_3(self):
        result = solution('d4')
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
