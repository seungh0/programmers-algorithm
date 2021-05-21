import collections
import unittest


def soluiton(arr):
    counts = collections.defaultdict(int)

    for num in arr:
        if counts[num] == 0:
            counts[num] = arr.count(num)

        if counts[num] > len(arr) // 2:
            return num


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = soluiton([3, 2, 3])
        self.assertEqual(result, 3)

    def test_something1(self):
        result = soluiton([2, 2, 1, 1, 1, 2, 2, ])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
