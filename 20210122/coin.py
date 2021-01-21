import unittest

d = [10000] * 10000


def solution(money, coins):
    d[0] = 0
    for i in coins:
        for j in range(coins[0], money + 1):
            if d[j - i] != 10000:
                d[j] = min(d[j], d[j - i] + 1)
    return d[money]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(15, [2, 3])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
