import unittest

INF = int(1e9)


def init_graph(n, a):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, len(graph)):
        graph[i][i] = 0

    for a, b in a:
        graph[a][b] = 1
        graph[b][a] = 1

    return graph


def solution(n, m, a, x, k):
    graph = init_graph(n, a)

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

    return graph[1][k] + graph[k][x]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 4],
            [3, 4],
            [3, 5],
            [4, 5]
        ]
        result = solution(5, 7, a, 4, 5)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
