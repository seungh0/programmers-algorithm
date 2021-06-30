import unittest


def dfs(graph, start, visited):
    result = []
    visited[start] = True
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            result += dfs(graph, i, visited)
    return result


def solution(graph):
    visited = [False] * len(graph)
    return dfs(graph, 1, visited)


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
            []
        ]
        result = solution(graph)
        self.assertEqual(result, [1, 2, 7, 6, 8, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
