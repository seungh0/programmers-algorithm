import unittest

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(graph, dx, dy, n):
    graph[dx][dy] = 0
    cnt = 1
    for mx, my in move:
        x, y = dx + mx, dy + my
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        if graph[x][y] == 1:
            cnt += bfs(graph, x, y, n)
    return cnt


def solution(n, graph):
    cnt = 0
    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result.append(bfs(graph, i, j, n))
                cnt += 1
    return cnt, result


# cnt = int(input())
# graph = []
# for i in range(cnt):
#     n = ' '.join(input())
#     graph.append(list((map(int, n.split(" ")))))
# cnt, result = solution(cnt, graph)
# print(cnt)
# result.sort()
# for i in result:
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


if __name__ == '__main__':
    unittest.main()
