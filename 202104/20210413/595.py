import unittest
import collections


def solution(tasks, n):
    counter = collections.Counter(tasks)
    result = 0
    while True:
        for task, _ in counter.most_common(n + 1):
            result += 1
            counter.subtract(task)
            counter += collections.Counter()
        if not counter:
            return result
        result += 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(['A', 'A', 'A', 'B', 'B', 'B'], 2)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
