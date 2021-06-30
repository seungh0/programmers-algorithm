import unittest
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def bfs(n, graph, result):
    q = []
    heappush(q, (0, 0, graph[0][0]))
    while q:
        x, y, value = heappop(q)
        for dx, dy in move:
            mx = x + dx
            my = y + dy
            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue
            v = value + graph[mx][my]
            if v < result[mx][my]:
                result[mx][my] = v
                q.append((mx, my, v))
    return result[n - 1][n - 1]


def solution(n, graph):
    result = [[1000] * n for _ in range(n)]
    return bfs(n, graph, result)


cnt = 1
result = []
while True:
    n = int(input())
    if n == 0:
        break
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split(" "))))
    result.append("Problem " + str(cnt) + ": " + str(solution(n, temp)))
    cnt += 1

for i in result:
    print(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        graph = [
            [5, 5, 4],
            [3, 9, 1],
            [3, 2, 7]
        ]
        result = solution(3, graph)
        self.assertEqual(result, 20)

    def test_something1(self):
        graph = [
            [3, 7, 2, 0, 1],
            [2, 8, 0, 9, 1],
            [1, 2, 1, 8, 1],
            [9, 8, 9, 2, 0],
            [3, 6, 5, 1, 5]
        ]
        result = solution(5, graph)
        self.assertEqual(result, 19)


if __name__ == '__main__':
    unittest.main()
