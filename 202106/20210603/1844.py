import unittest
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(maps):
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for mx, my in move:
            dx, dy = x + mx, y + my
            if dx < 0 or dy < 0 or dx >= len(maps) or dy >= len(maps[0]):
                continue
            if maps[dx][dy] == 0:
                continue
            if maps[dx][dy] == 1:
                maps[dx][dy] = maps[x][y] + 1
                queue.append((dx, dy))

    result = maps[len(maps) - 1][len(maps[0]) - 1]
    return -1 if result == 1 else result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1]
        ])
        self.assertEqual(result, 11)

    def test_something2(self):
        result = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]])
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
