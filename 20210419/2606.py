import unittest


def dfs(is_visited, graph, start):
    result = []
    is_visited[start] = True
    result.append(start)
    for i in graph[start]:
        if not is_visited[i]:
            result += dfs(is_visited, graph, i)
    return result


def solution(a, b, param):
    graph = [[] for _ in range(a + 1)]
    is_visited = [False] * (a + 1)
    for x, y in param:
        graph[x].append(y)
        graph[y].append(x)
    return len(dfs(is_visited, graph, 1)) - 1


a = int(input())
b = int(input())
param = []
for i in range(b):
    x, y = map(int, input().split())
    param.append((x, y))
print(solution(a, b, param))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(7, 6, [
            (1, 2),
            (2, 3),
            (1, 5),
            (5, 2),
            (5, 6),
            (4, 7)
        ])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
