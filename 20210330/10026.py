import unittest

import sys
sys.setrecursionlimit(10000)

import copy

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, n, graph):
    if graph[x][y] is False:
        return False

    value = graph[x][y]
    graph[x][y] = False

    for mx, my in move:
        dx, dy = x + mx, y + my
        if dx < 0 or dy < 0 or dx >= n or dy >= n or graph[dx][dy] is False:
            continue
        if graph[dx][dy] == value:
            dfs(dx, dy, n, graph)
    return True


def count(n, graph):
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if dfs(i, j, n, graph):
                cnt += 1
    return cnt


def convert(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'
    return graph


def solution(n, graph):
    temp = convert(copy.deepcopy(graph))
    return count(n, graph), count(n, temp)


# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(input()))
# x, y = solution(n, graph)
# print(x, y)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, [
            ['R', 'R', 'R', 'B', 'B'],
            ['G', 'G', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'R', 'R'],
            ['B', 'B', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R']
        ])
        self.assertEqual(result, (4, 3))

    def test_something1(self):
        result = solution(3, [
            ['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'R', 'R']
        ])
        self.assertEqual(result, (1, 1))

    def test_something2(self):
        result = solution(3, [
            ['R', 'R', 'R'],
            ['R', 'G', 'R'],
            ['R', 'G', 'R']
        ])
        self.assertEqual(result, (2, 1))


if __name__ == '__main__':
    unittest.main()
