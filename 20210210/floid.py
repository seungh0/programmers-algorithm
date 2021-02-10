import unittest

INF = int(1e9)


def solution(n, m, info):
    graph = init_graph(n, m, info)

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return make_result(n, graph)


def init_graph(n, m, info):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        graph[a][a] = 0

    for i in range(m):
        a, b, c = info[i]
        graph[a][b] = c
    return graph


def make_result(n, graph):
    result = []
    for a in range(1, n + 1):
        tmp = []
        for b in range(1, n + 1):
            tmp.append(graph[a][b])
        result.append(tmp)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        info = [
            [1, 2, 4],
            [1, 4, 6],
            [2, 1, 3],
            [2, 3, 7],
            [3, 1, 5],
            [3, 4, 4],
            [4, 3, 2]
        ]
        result = solution(4, 7, info)
        self.assertEqual(result, [
            [0, 4, 8, 6],
            [3, 0, 7, 9],
            [5, 9, 0, 4],
            [7, 11, 2, 0]
        ])


if __name__ == '__main__':
    unittest.main()
