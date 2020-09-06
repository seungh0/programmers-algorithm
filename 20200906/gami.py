import unittest


def solution(arr):
    d = [0] * 100
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        d[i] = max(d[i - 2] + arr[i], d[i - 1])
    return d[len(arr) - 1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [1, 3, 1, 5]
        result = solution(arr)
        self.assertEqual(result, 8)

    def test_something_2(self):
        arr = [99, 100, 99, 1]
        result = solution(arr)
        self.assertEqual(result, 198)

    def test_something_3(self):
        arr = [1, 99, 100, 300, 50, 30]
        result = solution(arr)
        self.assertEqual(result, 429)


if __name__ == '__main__':
    unittest.main()
