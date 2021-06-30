import unittest

_quest = []


def dfs(graph, v, visited):
    visited[v] = True
    _quest.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return _quest


class TestDfs(unittest.TestCase):
    def test_dfs(self):
        # given
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

        # when
        result = dfs(graph, 1, visited)

        # then
        self.assertEqual(result, [1, 2, 7, 6, 8, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
