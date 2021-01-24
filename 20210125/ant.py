import unittest

d = [0] * 101


def solution(arr):
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        d[i] = max((d[i - 2] + arr[i]), d[i - 1])
    return d[len(arr) - 1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 3, 1, 5])
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
