import unittest
import sys
import heapq

input = sys.stdin.readline

INF = 1e9


def dfs(n, graph, start):
    result = [INF] * (n + 1)
    result[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if result[node] > dist:
            continue

        for node, d in graph[node]:
            distance = dist + d

            if distance < result[node]:
                result[node] = distance
                heapq.heappush(q, (distance, node))
    return result


def init_graph(n, graph):
    g = [[] for _ in range(n + 1)]
    for x, y, dist in graph:
        g[x].append((y, dist))
    return g


def solution(n, m, start, graph):
    graph = init_graph(n, graph)
    result = dfs(n, graph, start)
    return result[1:]


def test():
    n, m = map(int, input().split(" "))
    start = int(input())
    result = []
    for i in range(m):
        result.append(map(int, input().split(" ")))
    answer = solution(n, m, start, result)

    for i in answer:
        if i == INF:
            print("INF")
        else:
            print(i)


test()


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
