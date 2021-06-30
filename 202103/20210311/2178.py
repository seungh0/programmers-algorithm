import unittest
from collections import deque

move = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def solution(n, m, graph):
    start = (0, 0, 1)
    queue = deque()
    queue.append(start)

    while queue:
        x, y, cnt = queue.popleft()
        for mx, my in move:
            dx = x + mx
            dy = y + my

            if dx < 0 or dy < 0 or dx >= n or dy >= m:
                continue

            if graph[dx][dy] == 1:
                graph[dx][dy] = cnt + 1
                queue.append((dx, dy, cnt + 1))

    return graph[n - 1][m - 1]


# n, m = map(int, input().split(" "))
# r = []
# for i in range(n):
#     t = []
#     word = map(int, input())
#     for w in word:
#         t.append(w)
#     r.append(t)
#
# print(solution(n, m, r))


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
