import unittest


def dfs(is_visited, graph, start):
    cnt = 0
    is_visited[start] = True
    for i in graph[start]:
        if not is_visited[i]:
            cnt += dfs(is_visited, graph, i)
    return cnt + 1


def solution(a, b, array):
    is_visited = [False] * (a + 1)
    graph = [[] for _ in range(a + 1)]
    for x, y in array:
        graph[x].append(y)
        graph[y].append(x)

    return dfs(is_visited, graph, 1) - 1


# n = int(input())
# m = int(input())
# array = []
# for i in range(m):
#     array.append(list(map(int, input().split())))
# print(solution(n, m, array))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(7, 6, [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
