import unittest
from collections import deque


def bfs(graph, start):
    distance = [-1] * (len(graph) + 1)
    distance[start] = 0

    q = deque([start])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                q.append(next)
    return distance


def init_graph(graph, city_num):
    g = [[] for i in range(city_num + 1)]
    for s, e in graph:
        g[s].append(e)
    return g


def calculate(distances, answer):
    result = []
    for i in range(len(distances)):
        if distances[i] == answer:
            result.append(i)
    if len(result) == 0:
        return -1
    return result


def solution(city_num, road_num, graph, answer, start):
    graph = init_graph(graph, city_num)
    distances = bfs(graph, start)
    return calculate(distances, answer)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = [
            [1, 2],
            [1, 3],
            [2, 3],
            [2, 4]
        ]
        result = solution(4, 4, graph, 2, 1)
        self.assertEqual(result, [4])

    def test_something1(self):
        graph = [
            [1, 2],
            [1, 3],
            [1, 4]
        ]
        result = solution(4, 3, graph, 2, 1)
        self.assertEqual(result, -1)

    def test_something2(self):
        graph = [
            [1, 2],
            [1, 3],
            [2, 3],
            [2, 4]
        ]
        result = solution(4, 4, graph, 1, 1)
        self.assertEqual(result, [2, 3])


if __name__ == '__main__':
    unittest.main()
