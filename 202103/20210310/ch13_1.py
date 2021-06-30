import unittest
from collections import deque


def bfs(graph, start):
    result = [100000] * len(graph)
    queue = deque()
    queue.append((start, 0))
    result[start] = 0

    while queue:
        city, distance = queue.popleft()
        for i in graph[city]:
            if result[i] > distance + 1:
                result[i] = distance + 1
                queue.append((i, distance + 1))
    return result


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
