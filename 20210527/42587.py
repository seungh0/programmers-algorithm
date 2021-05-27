import unittest
from collections import deque


def maxInQueue(queue, priority):
    for q, i in queue:
        if priority < q:
            return False
    return True


def findIndex(result, location):
    for i, r in enumerate(result):
        if r == location:
            return i + 1
    return -1


def solution(priorities, location):
    result = []
    queue = deque()
    for i, priority in enumerate(priorities):
        queue.append((priority, i))

    while queue:
        priority, index = queue.popleft()
        if maxInQueue(queue, priority):
            result.append(index)
            continue
        queue.append((priority, index))

    return findIndex(result, location)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([2, 1, 3, 2], 2)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
