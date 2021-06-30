import unittest


def dfs(graph, x, y):
    if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
        return False
    if graph[x][y] != 0:
        return False
    graph[x][y] = 1
    dfs(graph, x - 1, y)
    dfs(graph, x, y - 1)
    dfs(graph, x, y + 1)
    dfs(graph, x + 1, y)
    return True


def solution(param):
    result = 0
    for i in range(len(param)):
        for j in range(len(param[i])):
            if dfs(param, i, j):
                result += 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
