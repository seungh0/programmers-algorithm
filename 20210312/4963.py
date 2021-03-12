import unittest

move = [(-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(x, y, graph):
    if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0
    for dx, dy in move:
        dfs(x + dx, y + dy, graph)
    return True


def solution(n, m, graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j, graph):
                cnt += 1
    return cnt


# answer= []
#
# while True:
#     n, m = map(int, input().split(" "))
#     if n == 0 and m == 0:
#         break
#     r = []
#     for i in range(m):
#         r.append(list(map(int, input().split(" "))))
#     answer.append(solution(n, m, r))
#
# for i in answer:
#     print(i)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(1, 1, [
            [0]
        ])
        self.assertEqual(result, 0)

    def test_something1(self):
        result = solution(3, 2, [
            [1, 1, 1],
            [1, 1, 1]
        ])
        self.assertEqual(result, 1)

    def test_something2(self):
        result = solution(5, 4, [
            [1, 0, 1, 0, 0, ],
            [1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0]
        ])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
