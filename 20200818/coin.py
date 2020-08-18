import unittest


def solution(money):
    count = 0
    coin_list = [500, 100, 50, 10]
    for coin in coin_list:
        count += money // coin
        money %= coin
    return count


class CoinTest(unittest.TestCase):
    def test_case_1(self):
        money = 1260
        result = solution(money)
        self.assertEqual(result, 6)
