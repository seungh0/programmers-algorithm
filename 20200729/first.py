# 소수찾기 (Level2)
# https://programmers.co.kr/learn/courses/30/lessons/42839
import unittest
from itertools import permutations


def solution(numbers):
    cnt = 0
    temp = []
    for i in range(len(numbers)):
        temp += list(map(''.join, permutations(numbers, i + 1)))

    temp = list(set(map(int, temp)))

    for i in range(len(temp)):
        if isDecimal(temp[i]):
            cnt += 1
    return cnt


def isDecimal(number):
    number = int(number)
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


class TestIsDecimal(unittest.TestCase):
    def test_case_1(self):
        number = 10
        result = isDecimal(number)
        self.assertFalse(result)

    def test_case_2(self):
        number = 2
        result = isDecimal(number)
        self.assertTrue(result)

    def test_case_3(self):
        number = 7
        result = isDecimal(number)
        self.assertTrue(result)

    def test_case4(self):
        a = "01"
        self.assertEqual(int(a), 1)


class TestFirstSolution(unittest.TestCase):
    def test_case1(self):
        # given
        numbers = "17"
        # when
        result = solution(numbers)
        # then
        self.assertEqual(result, 3)

    def test_case2(self):
        # given
        numbers = "011"
        # when
        result = solution(numbers)
        # then
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
