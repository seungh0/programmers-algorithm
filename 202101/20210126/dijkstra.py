import unittest

INF = 1e9


def get_proximate_node(n, distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(n, graph, start, distance, visited):
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]
    for _ in range(n + 1):
        node = get_proximate_node(n, distance, visited)
        visited[node] = True
        for i in graph[node]:
            cost = distance[node] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
    return distance


def solution(n, graph):
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    start = 1
    distance = dijkstra(n, graph, start, distance, visited)
    result = []
    for i in range(1, n + 1):
        result.append(distance[i])
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 6
        graph = [
            [],
            [(2, 2), (3, 5), (4, 1)],
            [(3, 3), (4, 2)],
            [(2, 3), (6, 5)],
            [(3, 3), (5, 1)],
            [(3, 1), (6, 2)],
            []
        ]
        result = solution(n, graph)
        self.assertEqual(result, [0, 2, 3, 1, 2, 4])


if __name__ == '__main__':
    unittest.main()
