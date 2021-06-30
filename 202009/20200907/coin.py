import unittest


def solution(amount, coins):
    d = [10000] * (amount + 1)
    for coin in coins:
        d[coin] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            d[i] = min(d[i - coin] + 1, d[i])
    if d[amount] == 10000:
        return -1
    return d[amount]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        amount = 15
        coins = [2, 3]
        result = solution(amount, coins)
        self.assertEqual(result, 5)

    def test_something2(self):
        amount = 20
        coins = [2, 3]
        result = solution(amount, coins)
        self.assertEqual(result, 7)

    def test_something3(self):
        amount = 10
        coins = [2, 10]
        result = solution(amount, coins)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
