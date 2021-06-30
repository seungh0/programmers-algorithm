import unittest
import collections


def solution(tasks, n):
    counter = collections.Counter(tasks)
    cnt = 0
    while True:
        for task, _ in counter.most_common(n + 1):
            cnt += 1
            counter.subtract(task)
            counter += collections.Counter()
        if not counter:
            break
        cnt += 1
    return cnt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(['A', 'A', 'A', 'B', 'B', 'B'], 2)
        # A B 0 A B 0 A B
        self.assertEqual(result, 8)

    def test_something2(self):
        result = solution(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'], 3)
        # A B C 0 A B C 0 A B C
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
