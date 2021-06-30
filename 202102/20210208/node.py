import unittest
from collections import deque


def dijkstra(start, graph, distance, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[node] + 1
    return distance


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    for (a, b) in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    distance = dijkstra(0, graph, distance, visited)
    distance.sort(reverse=True)
    return distance.count(distance[0])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
        result = solution(6, vertex)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
