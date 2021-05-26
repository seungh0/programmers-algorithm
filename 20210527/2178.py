import unittest

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(n, m, graph):
    def bfs(x, y, cnt):
        if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
            return
        if graph[x][y] == 0 or graph[x][y] > 1:
            return
        graph[x][y] = cnt
        for mx, my in move:
            dx, dy = x + mx, y + my
            bfs(dx, dy, cnt + 1)

    bfs(0, 0, 1)

    return graph[n - 1][m - 1]


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
