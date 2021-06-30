import unittest

move = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def solution(graph):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]) or graph[x][y] == 0:
            return
        graph[x][y] = 0
        for mx, my in move:
            dx = x + mx
            dy = y + my
            dfs(dx, dy)

    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.assertEqual(result, 1)

    def test_something2(self):
        result = solution([
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
