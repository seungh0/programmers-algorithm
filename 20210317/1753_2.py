import unittest
import sys
import heapq

input = sys.stdin.readline

INF = 1e9


def dfs(n, start, graph):
    result = [INF] * (n + 1)
    result[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if dist > result[node]:
            continue

        for y, d in graph[node]:
            distance = dist + d
            if result[y] > distance:
                result[y] = distance
                heapq.heappush(q, (distance, y))
    return result[1:]


def solution(n, m, start, graph):
    g = [[] for i in range(n + 1)]
    for x, y, dist in graph:
        g[x].append((y, dist))
    return dfs(n, start, g)


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
