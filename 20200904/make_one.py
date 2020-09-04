import unittest

d = [0] * 10000


def solution(x):
    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[x]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 26
        result = solution(n)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
