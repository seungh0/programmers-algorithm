import unittest
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(a, b, map):
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for mx, my in move:
            dx, dy = x + mx, y + my
            if dx < 0 or dy < 0 or dx >= a or dy >= b:
                continue
            if map[dx][dy] != 1:
                continue
            map[dx][dy] = map[x][y] + 1
            queue.append((dx, dy))
    return map[a - 1][b - 1]


# x, y = map(int, input().split())
# array = []
# for _ in range(x):
#     array.append(list(map(int, list(input()))))
# print(solution(x, y, array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, 6, [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1]
        ])
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
