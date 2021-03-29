import unittest
import sys
from collections import deque

input = sys.stdin.readline


def dfs(start, graph, is_visited):
    result = []
    result.append(start)
    is_visited[start] = True

    for i in graph[start]:
        if not is_visited[i]:
            is_visited[i] = True
            result += dfs(i, graph, is_visited)
    return result


def dfs_solution(start, graph):
    is_visited = [False] * (len(graph) + 1)
    return dfs(start, graph, is_visited)


def bfs(start, graph, is_visited):
    result = []
    q = deque([start])
    result.append(start)
    is_visited[start] = True
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not is_visited[i]:
                q.append(i)
                is_visited[i] = True
                result.append(i)
    return result


def bfs_solution(start, graph):
    is_visited = [False] * (len(graph) + 1)
    return bfs(start, graph, is_visited)


def solution(n, m, start, array):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for s, e in array:
        graph[s][e] = 1
        graph[e][s] = 1
    print(graph)
    result_dfs = dfs_solution(start, graph)
    result_bfs = bfs_solution(start, graph)
    return [result_dfs, result_bfs]


# n, m, start = map(int, input().split())
# array = []
# for i in range(m):
#     array.append(list(map(int, input().split())))
# result = solution(n, m, start, array)
# for i in result:
#     for j in i:
#         print(j, end=" ")
#     print()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(4, 5, 1, [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 4],
            [3, 4]
        ])
        self.assertEqual(result, [
            [1, 2, 4, 3],
            [1, 2, 3, 4]
        ])

    def test_something1(self):
        result = solution(5, 5, 3, [
            [5, 4],
            [5, 2],
            [1, 2],
            [3, 4],
            [3, 1]
        ])
        self.assertEqual(result, [
            [3, 1, 2, 5, 4],
            [3, 1, 4, 2, 5]
        ])


if __name__ == '__main__':
    unittest.main()
