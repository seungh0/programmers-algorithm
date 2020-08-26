import unittest
from collections import deque

_quest = []


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        _quest.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return _quest


class TestBfs(unittest.TestCase):
    def test_bfs(self):
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
        result = bfs(graph, 1, visited)

        # then
        self.assertEqual(result, [1, 2, 3, 8, 7, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
