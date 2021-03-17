import unittest
import sys
import heapq

input = sys.stdin.readline

INF = 1e9


def init_graph(n, graph):
    g = [[] * n for _ in range(n + 1)]
    for start, end, dist in graph:
        g[start].append((end, dist))
    return g


def dfs(n, graph, start):
    result = [INF] * (n + 1)
    result[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        weight, node = heapq.heappop(q)

        if weight > result[node]:
            continue

        for n, w in graph[node]:
            distance = weight + w
            if distance < result[n]:
                result[n] = distance
                heapq.heappush(q, (distance, n))
    return result[1:]


def solution(n, m, start, graph):
    graph = init_graph(n, graph)
    return dfs(n, graph, start)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = [
            [5, 1, 1],
            [1, 2, 2],
            [1, 3, 3],
            [2, 3, 4],
            [2, 4, 5],
            [3, 4, 6]
        ]
        result = solution(5, 6, 1, graph)
        self.assertEqual(result, [0, 2, 3, 7, INF])

    def test_something1(self):
        graph = [
            [1, 2, 3],
            [1, 3, 5],
            [2, 3, 1]
        ]
        result = solution(3, 3, 1, graph)
        self.assertEqual(result, [0, 3, 4])


if __name__ == '__main__':
    unittest.main()
