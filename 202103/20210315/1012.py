import unittest
import sys

sys.setrecursionlimit(10000)

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(arr, x, y):
    if x < 0 or y < 0 or x >= len(arr) or y >= len(arr[0]):
        return False
    if arr[x][y] == 0:
        return False
    arr[x][y] = 0

    dfs(arr, x - 1, y)
    dfs(arr, x + 1, y)
    dfs(arr, x, y - 1)
    dfs(arr, x, y + 1)
    return True


def solution(n, m, cnt, graph):
    arr = [[0] * m for _ in range(n)]
    for x, y in graph:
        arr[x][y] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(arr, i, j):
                cnt += 1
    return cnt


result = []
n = int(input())
for i in range(n):
    x, y, cnt = map(int, input().split(" "))
    graph = []
    for i in range(cnt):
        graph.append(list(map(int, input().split(" "))))
    result.append(solution(x, y, cnt, graph))
for i in result:
    print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = [
            [0, 0],
            [1, 0],
            [1, 1],
            [4, 2],
            [4, 3],
            [4, 5],
            [2, 4],
            [3, 4],
            [7, 4],
            [8, 4],
            [9, 4],
            [7, 5],
            [8, 5],
            [9, 5],
            [7, 6],
            [8, 6],
            [9, 6]
        ]
        result = solution(10, 8, 17, graph)
        self.assertEqual(result, 5)

    def test_something1(self):
        graph = [
            [5, 5]
        ]
        result = solution(10, 10, 1, graph)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
