import unittest

INF = 1e9


def get_smallest_node(n, distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(n, start, graph, distance, visited):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node(n, distance, visited)
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    return distance


def solution(n, graph):
    visited = [False] * (n + 1)
    start = 1
    distance = [INF] * (n + 1)
    distance = dijkstra(n, start, graph, distance, visited)
    result = []
    for i in range(1, n + 1):
        result.append(distance[i])
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 6
        node = [
            [],
            [(2, 2), (3, 5), (4, 1)],  # 1
            [(3, 3), (4, 2)],  # 2
            [(2, 3), (6, 5)],  # 3
            [(3, 3), (5, 1)],  # 4
            [(3, 1), (6, 2)],  # 5
            []
        ]
        result = solution(n, node)
        self.assertEqual(result, [0, 2, 3, 1, 2, 4])


if __name__ == '__main__':
    unittest.main()
