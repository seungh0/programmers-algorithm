import unittest
from collections import deque


class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y


_directions = [
    Direction(1, 0),
    Direction(-1, 0),
    Direction(0, 1),
    Direction(0, -1)
]


def is_not_road(dx, dy, graph):
    if dx < 0 or dy < 0 or dx >= len(graph) or dy >= len(graph[0]):
        return True
    if graph[dx][dy] != 1:
        return True
    return False


def solution(graph, miro_entrance, miro_exit):
    start = miro_entrance
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        x, y = pos
        for i in range(len(_directions)):
            dx = x + _directions[i].x
            dy = y + _directions[i].y
            if is_not_road(dx, dy, graph):
                continue
            graph[dx][dy] = graph[x][y] + 1
            queue.append((dx, dy))
    return graph[miro_exit[0]][miro_exit[1]]


class TestSolution(unittest.TestCase):
    def test_solution_case(self):
        # given
        graph = [
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
        ]
        miro_entrance = (0, 0)
        miro_exit = (len(graph) - 1, len(graph[0]) - 1)

        # when
        result = solution(graph, miro_entrance, miro_exit)

        # then
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
