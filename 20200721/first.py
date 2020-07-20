# 주식 가격 (Level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42584
import unittest


def solution(prices):
    result = []
    for i in range(len(prices)):
        result.append(calculateSecond(prices, i))
    return result


def calculateSecond(prices, i):
    second = 0
    for j in range(i + 1, len(prices)):
        second += 1
        if prices[i] > prices[j]:
            break
        j += 1
    return second


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        prices = [1, 2, 3, 2, 3]
        # when
        result = solution(prices)
        # then
        self.assertEqual(result, [4, 3, 1, 1, 0])

    def test_case2(self):
        # given
        prices = [1]
        # when
        result = solution(prices)
        # then
        self.assertEqual(result, [0])

    def test_case3(self):
        # given
        prices = [3, 2, 1]
        # when
        result = solution(prices)
        # then
        self.assertEqual(result, [1, 1, 0])


if __name__ == '__main__':
    unittest.main()
