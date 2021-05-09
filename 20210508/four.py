import unittest


def solution(n, start, end, roads, traps):
    answer = 0
    distances = [[] for _ in range(n + 1)]
    reverse = [[] for _ in range(n + 1)]
    for start, end, dist in roads:
        distances[start].append((end, dist))
        reverse[end].append((start, dist))

    graph = distances
    for e, d in graph[start]:
        if e == end:
            return d

    return answer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
