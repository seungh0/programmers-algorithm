import unittest


def dfs(graph, start, is_visited):
    is_visited[start] = True
    result = []
    for i in graph[start]:
        if not is_visited[i]:
            result.append(i)
            result += dfs(graph, i, is_visited)
    return result


def solution(n, m, graph):
    g = [[] for _ in range(n + 1)]
    for s, e in graph:
        g[s].append(e)
        g[e].append(s)

    is_visited = [False] * (n + 1)
    return len(dfs(g, 1, is_visited))

# n = int(input())
# m = int(input())
# graph = []
# for i in range(m):
#     graph.append(map(int, input().split(" ")))
#
# print(solution(n, m, graph))


class MyTestCase(unittest.TestCase):

    def test_something1(self):
        result = solution(7, 6, [
            [1, 2],
            [2, 3],
            [1, 5],
            [5, 2],
            [5, 6],
            [4, 7]
        ])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
