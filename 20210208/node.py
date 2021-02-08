import unittest
from collections import deque

MAX = 1e9


def dijkstra(start, edge, distance, visited):
    queue = deque([])
    queue.append((start, 0))
    distance[start] = 0
    visited[start] = True
    while queue:
        start, cost = queue.popleft()
        visited[start] = True
        for i in edge:
            if i[0] == start and not visited[i[1]]:
                distance[i[1]] = min(distance[i[1]], distance[start] + 1)
                queue.append((i[1], cost + 1))
            if i[1] == start and not visited[i[0]]:
                distance[i[0]] = min(distance[i[0]], distance[start] + 1)
                queue.append((i[0], cost + 1))
    return distance


def solution(n, edge):
    distance = [MAX] * (n + 1)
    visited = [False] * (n + 1)
    distance = dijkstra(1, edge, distance, visited)
    max_value = max(distance[1:])
    return distance.count(max_value)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
        result = solution(6, vertex)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
