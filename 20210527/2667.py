import unittest

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def solution(n, graph):
    is_visited = [[False] * len(graph) for _ in range(len(graph))]
    answer = []

    def dfs(x, y):
        cnt = 0
        if x < 0 or y < 0 or x >= n or y >= n:
            return cnt
        if is_visited[x][y] or graph[x][y] == 0:
            return cnt
        is_visited[x][y] = True
        for mx, my in move:
            dx, dy = x + mx, y + my
            cnt += dfs(dx, dy)
        return cnt + 1

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if not is_visited[i][j] and graph[i][j] == 1:
                answer.append(dfs(i, j))
    answer.sort()
    return len(answer), answer


# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# length, result = solution(n, graph)
# print(length)
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
