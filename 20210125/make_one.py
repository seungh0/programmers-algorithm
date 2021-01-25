import unittest

d = [0] * 30000


def solution(n):
    for i in range(2, n + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[n]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(26)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()