import sys
import unittest


def solution(stocks):
    result = 0
    for i in range(len(stocks) - 1):
        for j in range(i + 1, len(stocks)):
            result = max(result, stocks[j] - stocks[i])
    return result


def solution1(stocks):
    profit = 0
    min_price = sys.maxsize

    for price in stocks:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)

    def test_something1(self):
        result = solution1([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
