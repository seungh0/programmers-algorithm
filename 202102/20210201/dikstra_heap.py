import unittest
import heapq

INF = 1e9


def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
    return distance


def solution(graph):
    distance = [INF] * len(graph)
    distance = dijkstra(1, graph, distance)
    result = []
    for i in range(1, len(distance)):
        result.append(distance[i])
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = [
            [],
            [(2, 2), (3, 5), (4, 1)],
            [(3, 3), (4, 2)],
            [(2, 3), (6, 5)],
            [(3, 3), (5, 1)],
            [(3, 1), (6, 2)],
            []
        ]
        result = solution(graph)
        self.assertEqual(result, [0, 2, 3, 1, 2, 4])


if __name__ == '__main__':
    unittest.main()
