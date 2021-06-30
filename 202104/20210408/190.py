import unittest
from collections import deque


def solution(nums):
    queue = deque(sorted(nums, reverse=True))
    result = 0
    while len(queue) > 1:
        left = queue.popleft()
        right = queue.popleft()
        result += right
    return result


def solution1(nums):
    nums.sort()
    result = 0
    for i, n in enumerate(nums):
        if i % 2 == 0:
            result += n
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 4, 3, 2])
        self.assertEqual(result, 4)

    def test_something1(self):
        result = solution1([1, 4, 3, 2])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
