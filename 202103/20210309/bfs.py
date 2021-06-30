import unittest
from collections import deque


def bfs(graph, start, visited):
    result = []
    queue = deque([start])
    visited[start] = True
    while queue:
        n = queue.popleft()
        result.append(n)
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return result


def solution(graph):
    visited = [False] * len(graph)
    return bfs(graph, 1, visited)


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
        result = solution(graph)
        self.assertEqual(result, [1, 2, 3, 8, 7, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
