import unittest
import collections
import sys

input = sys.stdin.readline


def dfs(graph, is_visited, start):
    cnt = 0
    q = collections.deque([start])
    is_visited[start] = True
    while q:
        x = q.popleft()
        for n in graph[x]:
            if not is_visited[n]:
                cnt += 1
                q.append(n)
                is_visited[n] = True
    return cnt


def solution(n, m, params):
    graph = [[] for _ in range(n + 1)]
    is_visited = [False for _ in range(n + 1)]
    for x, y in params:
        graph[x].append(y)
        graph[y].append(x)
    return dfs(graph, is_visited, 1)


# cnt = int(input())
# for _ in range(cnt):
#     array = []
#     n, m = map(int, input().split())
#     for _ in range(m):
#         array.append(list(map(int, input().split())))
#     print(solution(n, m, array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(3, 3, [
            [1, 2],
            [2, 3],
            [1, 3]
        ])
        self.assertEqual(result, 2)

    def test_something1(self):
        result = solution(5, 4, [
            [2, 1],
            [2, 3],
            [4, 3],
            [4, 5]
        ])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
