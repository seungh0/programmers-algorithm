import unittest
import heapq

INF = int(1e9)


def solution(city_num, road_num, target, info):
    graph, distance = init_graph(city_num, info)
    distance = dijkstra(target, graph, distance)
    return calculate(distance)


def init_graph(city_num, info):
    graph = [[] for _ in range(city_num + 1)]
    distance = [INF] * (city_num + 1)

    for x, y, sec in info:
        graph[x].append((y, sec))
    return graph, distance


def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[start]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


def calculate(distance):
    cnt = 0
    max_distance = 0
    for i in distance:
        if i != INF:
            cnt += 1
            max_distance = max(max_distance, i)
    return [cnt - 1, max_distance]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        info = [
            [1, 2, 4],
            [1, 3, 2]
        ]
        result = solution(3, 2, 1, info)
        self.assertEqual(result, [2, 4])


if __name__ == '__main__':
    unittest.main()
