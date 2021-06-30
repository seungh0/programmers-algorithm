import unittest
from collections import deque


def bfs(numbers, target):
    queue = deque([(0, 0)])
    result = 0
    while queue:
        v, cnt = queue.popleft()

        if cnt >= len(numbers):
            if v == target:
                result += 1
            continue

        one = v + numbers[cnt]
        two = v - numbers[cnt]
        queue.append((one, cnt + 1))
        queue.append((two, cnt + 1))

    return result


def solution(numbers, target):
    return bfs(numbers, target)


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        numbers = [1, 1, 1, 1, 1]
        result = solution(numbers, 3)
        self.assertEqual(result, 5)

    def test_something2(self):
        numbers = [1, 1]
        result = solution(numbers, 0)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
