import unittest
import collections

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(n, m, graph):
    result = [[1e9] * m for _ in range(n)]
    result[0][0] = 1
    queue = collections.deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        value = result[x][y]
        for mx, my in move:
            dx, dy = x + mx, y + my
            if dx < 0 or dy < 0 or dx >= n or dy >= m:
                continue
            if graph[dx][dy] == 0:
                continue
            if result[dx][dy] <= value + 1:
                continue
            result[dx][dy] = value + 1
            queue.append((dx, dy))
    return result[n - 1][m - 1]


# n, m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(list(map(int, list(input()))))
# print(solution(n, m, array))


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
