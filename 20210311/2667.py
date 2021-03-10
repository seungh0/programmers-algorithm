import unittest

move = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def dfs(graph, x, y):
    if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]) or graph[x][y] != 1:
        return 0
    graph[x][y] = 0
    cnt = 1
    for dx, dy in move:
        cnt += dfs(graph, x + dx, y + dy)
    return cnt


def solution(n, graph):
    r = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            cnt = dfs(graph, i, j)
            if cnt == 0:
                continue
            r.append(cnt)
    return len(r), sorted(r)


# n = int(input())
# graph = []
# for i in range(n):
#     t = []
#     for i in list(map(int, input())):
#         t.append(i)
#     graph.append(t)
#
# n, homes = solution(n, graph)
# print(n)
# for i in homes:
#     print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(7, [
            [0, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0]
        ])
        self.assertEqual(result, (3, [7, 8, 9]))

    def test_something1(self):
        result = solution(3, [
            [1, 0, 0],
            [0, 0, 1],
            [1, 1, 1]
        ])
        self.assertEqual(result, (2, [1, 4]))


if __name__ == '__main__':
    unittest.main()
