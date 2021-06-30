import unittest


def dfs(graph, index, visited):
    visited[index] = True
    for j in range(len(graph[index])):
        if j == index or visited[j] or graph[index][j] != 1:
            continue
        dfs(graph, j, visited)


def solution(n, computers):
    visited = [False] * n
    cnt = 0
    while False in visited:
        index = visited.index(False)
        dfs(computers, index, visited)
        cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        computers = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1]
        ]
        result = solution(3, computers)
        self.assertEqual(result, 2)

    def test_something2(self):
        computers = [
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1]
        ]
        result = solution(3, computers)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
