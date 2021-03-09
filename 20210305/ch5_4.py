import unittest
from collections import deque

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            pos_x = x + dx
            pos_y = y + dy
            if pos_x < 0 or pos_y < 0 or pos_x >= len(graph) or pos_y >= len(graph[0]):
                continue
            if graph[pos_x][pos_y] == 1:
                graph[pos_x][pos_y] += graph[x][y]
                queue.append((pos_x, pos_y))
    return graph[len(graph) - 1][len(graph[0]) - 1]


def solution(graph):
    return bfs(graph, 0, 0)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
        ])
        self.assertEqual(result, 10)

    if __name__ == '__main__':
        unittest.main()
