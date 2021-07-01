import unittest
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(node, graph, is_visited):
    is_visited[node] = True
    for i in graph[node]:
        if not is_visited[i]:
            dfs(i, graph, is_visited)


def solution(n, m, nodes):
    graph = [[] for _ in range(n + 1)]
    for start, end in nodes:
        graph[start].append(end)
        graph[end].append(start)

    cnt = 0
    is_visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not is_visited[i]:
            dfs(i, graph, is_visited)
            cnt += 1
    return cnt


# n, m = map(int, input().split())
# nodes = []
# for i in range(m):
#     nodes.append(map(int, input().split()))
# print(solution(n, m, nodes))


class MyTestCase(unittest.TestCase):
    def test_something0(self):
        result = solution(0, 0, [
        ])
        self.assertEqual(result, 0)

    def test_something1(self):
        result = solution(6, 5, [
            (1, 2),
            (2, 5),
            (5, 1),
            (3, 4),
            (4, 6)
        ])
        self.assertEqual(result, 2)

    def test_something2(self):
        result = solution(6, 8, [
            (1, 2),
            (2, 5),
            (5, 1),
            (3, 4),
            (4, 6),
            (5, 4),
            (2, 4),
            (2, 3)
        ])
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
