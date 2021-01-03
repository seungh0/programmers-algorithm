import unittest
from collections import deque

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_out_of_range(arr, x, y):
    if x < 0 or x >= len(arr) or y < 0 or y >= len(arr[0]):
        return True
    elif arr[x][y] != 1:
        return True
    return False


def solution(arr, x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for move_x, move_y in move:
            dx = x + move_x
            dy = y + move_y
            if is_out_of_range(arr, dx, dy):
                continue
            arr[dx][dy] = arr[x][y] + 1
            queue.append((dx, dy))
    return arr[len(arr) - 1][len(arr[0]) - 1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
        ]
        result = solution(arr, 0, 0)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
