import unittest


def dfs(graph, v, visited):
    result = []
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            result += dfs(graph, i, visited)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = [
            [],
            [2, 3, 8],
            [1, 7],
            [1, 4, 5],
            [3, 5],
            [3, 4],
            [7],
            [2, 6, 8],
            [1, 7]
        ]
        visited = [False] * 9
        result = dfs(graph, 1, visited)
        self.assertEqual(result, [1, 2, 7, 6, 8, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
