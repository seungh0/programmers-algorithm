import unittest
from collections import deque

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(n, m, array):
    result = [[1e9] * m for _ in range(n)]
    result[0][0] = 1
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        value = result[x][y]
        for dx, dy in move:
            mx, my = x + dx, y + dy
            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue
            if array[mx][my] == 1 and result[mx][my] > value + 1:
                result[mx][my] = value + 1
                q.append((mx, my))
    return result[n - 1][m - 1]


n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, list(input()))))
print(solution(n, m, array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, 6, [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1]
        ])
        self.assertEqual(result, 15)

    def test_something1(self):
        result = solution(4, 6, [
            [1, 1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1]
        ])
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
